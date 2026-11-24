const content = require('../../services/content')
const favorites = require('../../services/favorites')

Page({
  data: { count: 0 },

  onShow() {
    this.setData({ count: favorites.listIds().filter(id => content.get(id)).length })
  },
})
