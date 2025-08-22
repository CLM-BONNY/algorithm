from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    music = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        music[genre].append((i, play))
    
    genre_order = sorted(
        music.items(),
        key=lambda kv: sum(p for _, p in kv[1]),
        reverse=True
    )

    for g, songs in genre_order:
        songs_sorted = sorted(songs, key=lambda t: (-t[1], t[0]))
        answer.extend(i for i, _ in songs_sorted[:2])
        
    return answer