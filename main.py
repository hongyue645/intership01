# run .\venv\Scripts\Activate.ps1
# run python main.py
import asyncio
from xiaohongshu_mcp import (
    login,
    search_notes,
    get_note_content,
    get_note_comments,
    post_smart_comment
)
async def main():
    # 1.登录
    msg = await login()
    

    # 2.搜索
    results = await search_notes("美食", 3)
    print(results)

    # 3.获取URL
    first_url = results.split("链接: ")[1].split("\n")[0]
    print("---第一条笔记的URL---")
    print(first_url)

    # 4. 获取笔记内容
    content = await get_note_content(first_url)
    print("\n---第一条笔记的内容---")
    print(content)

    # 5.获取笔记评论
    comments = await get_note_comments(first_url)
    print("\n---第一条笔记的评论---")
    print(comments)

    # 6.发布一条智能评论
    smartComment = await post_smart_comment(first_url, "咨询")
    print("\n---发布的评论结果---")
    print(smartComment)


if __name__ == "__main__":
    asyncio.run(main())
