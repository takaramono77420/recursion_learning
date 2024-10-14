def websitePagination(urls,pageSize,page):
    # 関数を完成させてください

    pageUrls = [[]]
    pageNumber = 0

    for i, url in enumerate(urls):
        
        if i % pageSize == 0 and i != 0:
            pageNumber += 1
            pageUrls.append([])

        pageUrls[pageNumber].append(url)

    return pageUrls[page - 1]
