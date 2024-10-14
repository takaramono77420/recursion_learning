def videosToWatch(time,dailyGoal):
    # 関数を完成させてください
    totalMovieTime = 0
    for movie_time in time:
        totalMovieTime += movie_time
        if totalMovieTime >= dailyGoal:
            return time.index(movie_time) + 1
    
    return -1
        