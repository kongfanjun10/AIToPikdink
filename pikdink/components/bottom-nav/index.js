const tabs = [
  {
    "id": "home",
    "name": "首页",
    "icon": "⌂"
  },
  {
    "id": "news",
    "name": "资讯",
    "icon": "▤"
  },
  {
    "id": "tutorials",
    "name": "教学",
    "icon": "▷"
  },
  {
    "id": "courts",
    "name": "场地",
    "icon": "◇"
  },
  {
    "id": "gear",
    "name": "装备",
    "icon": "▱"
  },
  {
    "id": "profile",
    "name": "我的",
    "icon": "◎"
  }
]

Component({
  properties: {
    active: String,
  },
  data: { tabs },
})
