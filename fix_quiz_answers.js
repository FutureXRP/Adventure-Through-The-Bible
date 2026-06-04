#!/usr/bin/env node
// Run: node fix_quiz_answers.js stories.json
// Fixes 21 quiz questions where answer:3 references a non-existent 4th option
// on 3-option questions. Correct answer is always index 2 (the third option).

const fs = require('fs');
const path = require('path');

const filePath = process.argv[2] || 'stories.json';
if (!fs.existsSync(filePath)) {
  console.error('File not found:', filePath);
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

// Map of story ID -> array of 1-based question numbers that need fixing
const fixes = {
  'cain-abel':       [2],
  'noah':            [1],
  'tower-babel':     [3],
  'joseph':          [3],
  'moses-birth':     [1],
  'burning-bush':    [2],
  'red-sea':         [3],
  'gideon':          [2],
  'ruth':            [1],
  'samuel':          [3],
  'psalm23':         [3],
  'elijah':          [1],
  'daniel':          [2],
  'esther':          [3],
  'sermon-mount':    [2],
  'prodigal':        [1],
  'lazarus':         [3],
  'resurrection':    [3],
  'pentecost':       [1],
  'paul-conversion': [2],
  'paul-jail':       [3],
};

let fixed = 0;
let errors = [];

data.stories.forEach(story => {
  const storyFixes = fixes[story.id];
  if (!storyFixes) return;

  storyFixes.forEach(qNum => {
    const q = story.quiz && story.quiz[qNum - 1];
    if (!q) { errors.push(story.id + ' Q' + qNum + ': question not found'); return; }

    // Verify: answer should be 3, options count should be 3
    if (q.answer !== 3) {
      errors.push(story.id + ' Q' + qNum + ': expected answer=3, found answer=' + q.answer);
      return;
    }
    if (q.options.length !== 3) {
      errors.push(story.id + ' Q' + qNum + ': expected 3 options, found ' + q.options.length);
      return;
    }

    // Apply fix
    const correctAnswer = q.options[2];
    q.answer = 2;
    fixed++;
    console.log('Fixed ' + story.id + ' Q' + qNum + ': "' + correctAnswer.substring(0, 60) + '"');
  });
});

if (errors.length) {
  console.error('\nErrors:');
  errors.forEach(e => console.error('  ', e));
  process.exit(1);
}

// Write backup then save
const backupPath = filePath.replace('.json', '.backup.json');
fs.copyFileSync(filePath, backupPath);
fs.writeFileSync(filePath, JSON.stringify(data, null, 2));

console.log('\n✓ Fixed ' + fixed + ' questions in ' + filePath);
console.log('  Backup saved to ' + backupPath);

// Verify no bugs remain
let remaining = 0;
data.stories.forEach(story => {
  (story.quiz || []).forEach((q, qi) => {
    if (q.answer >= q.options.length) {
      remaining++;
      console.error('STILL BROKEN: ' + story.id + ' Q' + (qi+1));
    }
  });
});
if (remaining === 0) console.log('  Verification: all quiz answers are now in range ✓');
