const content = require('../../services/content')
const favorites = require('../../services/favorites')

Page({
  data: { item: null, isFavorite: false, isPreviewOpen: false },

  onLoad(options) {
    const item = content.get(options.id)
    if (item) this.setData({ item, isFavorite: favorites.listIds().includes(item.id) })
  },

  toggleFavorite() {
    try {
      this.setData({ isFavorite: favorites.toggle(this.data.item.id) })
    } catch {
      wx.showToast({ title: '保存失败，请重试', icon: 'none' })
    }
  },

  previewImage() {
    this.setData({ isPreviewOpen: true })
  },

  closePreview() {
    this.setData({ isPreviewOpen: false })
  },

  onShareAppMessage() {
    const item = this.data.item
    return item
      ? { title: item.title, path: '/pages/detail/index?id=' + item.id }
      : { title: '匹小将', path: '/pages/home/index' }
  },
})
