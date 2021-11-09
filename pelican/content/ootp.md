Title: ootp
Date: 2000-01-01 00:00

# Out of the Park Baseball Simulator

## Overview

Out of the Park Baseball Simulator (OOTP) is a
game with a realistic baseball game simulation engine
and comprehensive historical data. It is very flexible
and has many adjustable parameters. The program also offers
many ways of exporting data from the games that it simulates.

## Exhibition Games

OOTP has several simulation modes. To simulate a single
Word Series game, we run OOTP in Exhibition Mode. We can
set up an exhibition game between any two historical teams,
but we can also pick a particular World Series matchup.
We can also set up an exhibition match that is a single game.
We set the roster to 17 players, to match the number of
players that were on the field during the real Game 3.
The remaining players are benched, to ensure realistic
rotations during the games (for example, not having the
Game 4 starters come into the game to pitch in relief).

![Screenshot of OOTP setup for exhibition match between 1997 World Series teams.](/img/ootp1.png)

![Screenshot of OOTP setup for Infinite Cleveland exhibition matches.](/img/ootp2.png)

## Roster Setup

The roster takes a bit of work to set up correctly, but it only needs
to be done once - we'll freeze the game state once we set up the rosters
and before we start the game, and create a copy of the game for each
new simulation/timeline.

We obtained the roster of players used in Game 3 of the 1997 World Series
from [baseball-reference.com (link)](https://www.baseball-reference.com/boxes/CLE/CLE199710210.shtml).

**Rosters Tab:**

To set up the rosters for the game, we started at the Rosters tab.
Players that were in Game 3 were moved to the left side (active roster),
while players that were not in Game 3 were moved to the right side
(reserve roster).

From baseball-reference.com we can get the list of players and pitchers who
participated in the game, the batting order, and the positions each player was at:

![Screenshot of baseball-reference.com Florida Marlins lineup for 1997 World Series Game 3.](/img/baseballreference1.png)

Next, we organize the left/right sides of the roster page. Here is a screenshot
of the Florida Marlins roster with Game 3 players active:

![Screenshot of OOTP roster for 1997 Florida Marlins in World Series Game 3.](/img/ootp3.png)

**Lineups Tab:**

To arrange which players play at which positions, move to the Lineups tab.
Set the starting pitchers (Al Leiter for the Marlins, Charles Nagy for the Indians)
and a 1-man rotation, so that all other pitchers will be in the bullpen.
Next, set the batting lineup to be identical to the Game 3 batting lineup,
and put each player at the corresponding position. Here is a screenshot of
the batting lineup for the Florida Marlins, set up with Game 3 players:

![Screenshot of OOTP lineup for 1997 Florida Marlins in World Series Game 3.](/img/ootp4.png)

**Play Ball! Tab:**

Once the lineups are set, click the Play Ball! tab, and you'll see the green buttons to
either "Play" (watch the game as it is simulated) or "Simulate" (get an instantaneous
simulation).

Before clicking either, click "Return to OOTP Main Screen". The game state will be automatically saved,
no lineups or rosters will be lost.

(If you go to Saved Games from the OOTP Main Screen, you should see the Historical Exhibition
match automatically saved under the name "HistoricalExhibition" or "HistoricalExhibition.lg".)

## Copying a Saved Game

Now that the game has the correct teams and lineups, and has been saved prior to any
simulations being run, we can do some grunt work on the command line or in the folder
explorer to stash a copy of the unsimulated World Series Game 3, and create new copies
of that original each time we want to generate a new timeline.

Start by locating the directory where OOTP stores application data; it should be listed
somewhere in the game's Settings panel. On a Mac, the application's data directory is here:

```
$ cd "/Users/<username>/Library/Application Support/Out of the Park Developments/OOTP Baseball 20"
```

There are many files and parameters contained in this folder, but here we only cover how to
generate copies of a single frozen saved game.

The directory `saved_games` contains the saved games, which are contained in folders with an
`.lg` extension. By default, the exhibition match we created and automatically saved when
we jumped to the OOTP Main Screen will be called `HistoricalExhibition.lg`.

There is also a `saved_games.dat` file, which contains references to all of the saved games
(and is used to create the list of saved games on the OOTP main screen). The `saved_games.dat` file
must be consistent with the saved games that are present - if it contains a reference to
`KentuckyMinorLeagueSeason.lg`, then that save file must be present or OOTP will get confused.

However, fortunately for game hackers, this file can be deleted, and OOTP will automatically
check the contents of `saved_games` and create a new `saved_games.dat` for us. That means we can
move our clean, unsimulated `HistoricalExhibition.lg` game to a stash directory, and we can
create a brand new game/timeline as follows:

* Remove or rename `saved_games` if it exists
* Create a new, empty directory named `saved_games` in the OOTP data directory
* Copy `HistoricalExhibition.lg` (the clean, unsimulated game) into the new, empty `saved_games` directory
* Start up OOTP Baseball Simulator; this will automatically create a `saved_games.dat` file
* Click "Load Game" and load up your clean, unsimulated exhibition game with correct rosters and lineups.

## Timeline Generation Assembly Line

Once you've created your clean, unsimulated game, it takes a minute or less to perform the steps above,
load up the clean, unsimulated game, click the green "Simulate Game" button, and then click
"Return to OOTP Home Screen" (which will automatically save the outcome of the game that was
just simulated). The entire state of the simulator is stored in the save file, so once the
game is simulated and saved, you can stash that directory.

Once you have a saved game stashed away, you can come back to it by moving it back into `saved_games` and
re-opening the saved game in OOTP. You can perform tasks like replying the game in the 3D simulator,
generating an almanac (collection of HTML pages with information about teams, players, and games),
or exporting statistical data about the exhibition game to CSV files.

