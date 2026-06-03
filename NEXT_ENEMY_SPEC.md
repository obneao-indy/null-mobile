# NULL Next Enemy Spec

Updated: 2026-06-03

This document is a working sheet for deciding the next enemy with GPT before implementation.

## Current Game Baseline

`NULL` is a mobile-first auto-shooting dodge action game.

- Player moves by drag on mobile and WASD on PC.
- Player attacks automatically.
- Player has 3 HP pips.
- Battle timer is 90 seconds.
- The player gains equipment and skills from enemy rewards.
- Current equipment:
  - `EQ_001` / `単発弾` / single shot
  - `EQ_002` / `散弾` / 3-way shot
- Current skill:
  - `SK_001` / `巨大化` / bullet size +50% for 3 seconds
- Current stages:
  - `STAGE_001` / `Black Circle`
  - `STAGE_002` / `Triple Circle`, unlocked by clearing `Black Circle` with no damage

## Design Goal For The Next Enemy

The next enemy should add a new combat lesson without making the game feel noisy.

Preferred direction:

- Keep the visual language minimal: circles, simple shapes, monochrome plus small accent colors.
- Give the enemy one clear identity.
- Make the player move differently from `Black Circle`.
- Make the enemy readable on a phone screen.
- Avoid long text explanations during play.

## Candidate Enemy Slot

Working ID:

```text
ENE_002
```

Working stage ID:

```text
STAGE_003
```

Working name:

```text
TBD
```

Short player-facing label:

```text
TBD / HP ? / PATTERN ? / DROP ?
```

## Enemy Concept Questions

Use these questions with GPT to decide the enemy.

1. What should the enemy teach?
   - Precision dodging
   - Aggressive close-range play
   - Patience and timing
   - Using skills at the right moment
   - Managing multiple threats

2. What should the enemy feel like?
   - Fast and nervous
   - Heavy and oppressive
   - Tricky and evasive
   - Calm but dangerous
   - Weak alone, dangerous over time

3. How should the player beat it?
   - Stay close for better hit accuracy
   - Bait attacks, then punish
   - Circle around it
   - Survive burst phases
   - Use a specific equipment or skill

## Proposed Enemy Archetypes

Choose one or combine carefully.

### Fast Circle

Purpose: tests movement control and tracking.

- Low HP
- High movement speed
- Shoots narrow aimed shots
- Dodges player bullets more often than `Black Circle`
- Good drop candidate: movement or cooldown skill

### Heavy Circle

Purpose: tests patience and sustained dodging.

- High HP
- Slow movement
- Large slow bullets
- Occasional radial burst
- Good drop candidate: shield or piercing shot

### Split Circle

Purpose: introduces phase changes.

- Medium HP
- At 50% HP, splits into two smaller circles
- Each smaller circle shoots fewer bullets
- Good drop candidate: multi-shot or clone-like effect

### Orbit Circle

Purpose: tests positioning.

- Medium HP
- Has small orbiting bullets or satellites
- Main body shoots less often
- Good drop candidate: orbiting shield or pickup magnet

## Spec Template

Fill this section once the enemy is chosen.

### Identity

- Enemy ID:
- Stage ID:
- Display name:
- Enemy select label:
- Unlock condition:
- First-clear reward:

### Stats

```js
{
  hp: 0,
  speedRatio: 0,
  size: 0,
  attackCT: 0,
  bulletSpeed: 0,
  bulletSize: 0
}
```

Recommended starting ranges:

- HP: `8` to `18`
- Speed ratio: `0.45` to `1.15`
- Attack cooldown: `0.45` to `1.2`
- Bullet speed: `140` to `240`
- Bullet size: `5` to `11`

### Movement

Describe the movement in one sentence:

```text
TBD
```

Implementation notes:

- Does it chase the player?
- Does it keep distance?
- Does it dodge player bullets?
- Does it use burst movement?
- Does it stay in a lane or orbit?

### Attack Pattern

Describe the attack in one sentence:

```text
TBD
```

Pattern parameters:

```js
{
  attackAngles: [],
  burstCount: 0,
  burstInterval: 0,
  specialCT: 0,
  specialDuration: 0
}
```

### Phase Changes

Does the enemy change behavior by HP?

```text
None / 50% HP / 30% HP / timed phase
```

Phase details:

```text
TBD
```

### Drops

Drop intent:

```text
TBD
```

Drop table:

```js
[
  { type: "skill", id: "SK_???", chance: 0.00, maxOwn: 0 },
  { type: "equip", id: "EQ_???", chance: 0.00, maxOwn: 0 }
]
```

### Balance Targets

For a fresh player with only `単発弾`:

- Expected clear rate:
- Expected clear time:
- Expected damage taken:

For a player with `散弾` and `巨大化`:

- Expected clear rate:
- Expected clear time:
- Expected damage taken:

## Implementation Checklist

- Add enemy data.
- Add stage data.
- Add enemy select card.
- Add unlock condition.
- Add movement behavior.
- Add attack behavior.
- Add reward/drop data.
- Test on mobile viewport.
- Test locked and unlocked states.
- Test retry from defeat/pause keeps the same stage.
- Push `main`.
- Push or deploy `gh-pages`.

## GPT Prompt For Deciding The Enemy

Use this prompt when brainstorming:

```text
We are designing the next enemy for NULL, a mobile-first minimalist auto-shooting dodge action game.

Current enemy:
- Black Circle: HP 10, 3-way aimed shots, simple chase/spacing movement, mild bullet dodge.

Current progression:
- Triple Circle stage unlocks after a no-damage Black Circle clear.
- Player has single shot, scatter shot, and a bullet-size skill.

Suggest one next enemy that adds a new combat lesson while staying readable on a phone screen.
Give:
1. Enemy name
2. Visual identity
3. Movement behavior
4. Attack pattern
5. HP/speed/cooldown starting values
6. Unlock condition
7. Drop reward
8. Why it improves the game balance
```

