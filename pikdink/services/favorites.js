const storageKey = 'pikdink.favoriteIds'

function listIds() {
  const saved = wx.getStorageSync(storageKey)
  return Array.isArray(saved) ? saved : []
}

function toggle(id) {
  const ids = listIds()
  const isFavorite = !ids.includes(id)
  const updatedIds = isFavorite ? [id, ...ids] : ids.filter(savedId => savedId !== id)
  wx.setStorageSync(storageKey, updatedIds)
  return isFavorite
}

module.exports = { listIds, toggle }
