const content = require('../../services/content')
const favorites = require('../../services/favorites')

Page({
  data: { items: [] },

  onShow() {
    this.setData({ items: favorites.listIds().map(content.get).filter(Boolean) })
  },
})
