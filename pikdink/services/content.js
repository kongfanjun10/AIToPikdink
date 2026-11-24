const sections = [
  { id: 'news', name: '资讯', description: '看看球友圈最近聊什么。' },
  { id: 'tutorials', name: '教学', description: '从认识球拍到打出第一场对拉。' },
  { id: 'courts', name: '场地', description: '浏览不同类型的匹克球场。' },
  { id: 'gear', name: '装备', description: '了解球拍、球和其他上场装备。' },
]

const items = [
  {
    id: 'first-game',
    type: 'tutorials',
    category: '新手入门',
    title: '匹克球新手入坑指南',
    summary: '第一次上场，从握拍、发球到完成一次对拉。',
    image: '/assets/images/guides.jpg',
    paragraphs: [
      '先找一位球友练习短距离对拉，放慢挥拍速度，感受球拍触球的位置。',
      '上场前了解发球、双弹跳和非截击区规则，再从简单的接发球练习开始。',
    ],
  },
  {
    id: 'indoor-court',
    type: 'courts',
    category: '室内球场',
    title: '第一次去室内球场',
    summary: '球场选择和到场前准备。',
    image: '/assets/images/courts.jpg',
    paragraphs: [
      '约球前可以向场馆确认场地数量、开放时段、预约方式和是否提供球拍租借。',
      '这是室内球场的示例条目，图片用于展示场地卡片。',
    ],
  },
  {
    id: 'community',
    type: 'news',
    category: '球友动态',
    title: '周末和球友打场匹克球',
    summary: '从双打练习到社区友谊赛，认识几种常见的活动形式。',
    image: '/assets/images/news.jpg',
    paragraphs: [
      '新手可以先参加球友组织的体验活动，提前确认活动是否提供教学及装备。',
      '想要加入双打练习，可以先和搭档商量站位、换边以及谁负责中间来球。',
    ],
  },
  {
    id: 'paddle',
    type: 'gear',
    category: '球拍',
    title: '第一支球拍怎么选',
    summary: '试一试握柄粗细、挥拍手感和拍面的触球反馈。',
    image: '/assets/images/gear.jpg',
    paragraphs: [
      '试拍时做几次正反手挥拍，确认握柄大小和球拍重量适合自己。',
      '如果有租拍机会，可以先试几种不同的球拍，再决定购买。',
    ],
  },
].map(item => ({
  ...item,
  typeName: sections.find(section => section.id === item.type).name,
}))

function list(type) {
  return type ? items.filter(item => item.type === type) : items.slice()
}

function get(id) {
  return items.find(item => item.id === id)
}

function search(query) {
  const keyword = query.trim().toLowerCase()
  if (!keyword) return []

  return items.filter(item => [item.title, item.summary, item.category, item.typeName]
    .some(value => value.toLowerCase().includes(keyword)))
}

module.exports = { sections, list, get, search }
