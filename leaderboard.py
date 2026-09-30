# leaderboard.py
# Module 3: scores, rankings and statistics (kept in memory during the session)

import utils

# Every finished game is stored as a tuple: (player name, game name, score)
records = []


def add_score(name, game, score):
    """Save one finished game."""
    records.append((name, game, score))


def player_totals():
    """Return a dictionary: player name -> total score."""
    totals = {}
    for record in records:
        name = record[0]
        if name in totals:
            totals[name] = totals[name] + record[2]
        else:
            totals[name] = record[2]
    return totals


def sort_descending(items):
    """Selection sort for (name, total) tuples, highest total first."""
    items = items[:]
    n = len(items)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if items[j][1] > items[best][1]:
                best = j
        items[i], items[best] = items[best], items[i]
    return items


def highest_score():
    """Return the record (name, game, score) with the biggest score."""
    if len(records) == 0:
        return None
    top = records[0]
    for record in records:
        if record[2] > top[2]:
            top = record
    return top


def average_score():
    """Average score of all games played."""
    if len(records) == 0:
        return 0
    total = 0
    for record in records:
        total = total + record[2]
    return round(total / len(records), 1)


def kth_best_score(k):
    """Return the kth best single-game score (1 = best), or None."""
    scores = []
    for record in records:
        scores.append(record[2])
    if k < 1 or k > len(scores):
        return None
    # Remove the current biggest k-1 times; the biggest left is the answer
    for _ in range(k - 1):
        biggest = scores[0]
        for s in scores:
            if s > biggest:
                biggest = s
        scores.remove(biggest)
    answer = scores[0]
    for s in scores:
        if s > answer:
            answer = s
    return answer


def unique_players():
    """Return a set of player names (a set removes duplicates)."""
    names = set()
    for record in records:
        names.add(record[0])
    return names


def games_count():
    """Return a dictionary: game name -> how many times it was played."""
    counts = {}
    for record in records:
        game = record[1]
        if game in counts:
            counts[game] = counts[game] + 1
        else:
            counts[game] = 1
    return counts


def split_by_average(totals):
    """Partition players into two lists: above average total and the rest."""
    grand = 0
    for name in totals:
        grand = grand + totals[name]
    average = grand / len(totals)
    above = []
    rest = []
    for name in totals:
        if totals[name] > average:
            above.append(name)
        else:
            rest.append(name)
    return above, rest


def show_leaderboard():
    """Print the ranked table of players."""
    utils.print_title("LEADERBOARD")
    if len(records) == 0:
        print("No scores yet. Play a game first!")
        return
    ranked = sort_descending(list(player_totals().items()))
    print("Rank  Player        Total")
    print("-" * 28)
    rank = 1
    for item in ranked:
        print(str(rank).ljust(6) + item[0].ljust(14) + str(item[1]))
        rank = rank + 1


def show_stats():
    """Print statistics about all games played."""
    utils.print_title("STATISTICS")
    if len(records) == 0:
        print("No games played yet.")
        return
    top = highest_score()
    print("Games played:", len(records))
    print("Different players:", len(unique_players()))
    print("Average score per game:", average_score())
    print("Highest score:", top[2], "by", top[0], "in", top[1])
    second = kth_best_score(2)
    if second is not None:
        print("Second best score:", second)
    counts = games_count()
    for game in counts:
        print(" ", game, "played", counts[game], "time(s)")
    above, rest = split_by_average(player_totals())
    print("Above average players:", above)
    print("Others:", rest)


