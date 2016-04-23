<template>
  <div class="container read__next">
    <div class="row">
      <div class="col-xs-12">
        <h2 class="read__next-title">
          What to Read Next?
        </h2>

        <div class="row">
          <div class="col-xs-12 col-sm-6 col-md-3 text-center read__next-item"
            v-for="nextArticle in nextArticles">
            <a class="read__next-item-image"
              v-link="{ name: 'articleDetail', params: { articleId: nextArticle.id } }"
              title="{{ nextArticle.title }}">
              <img v-bind:src="nextArticle.hero_image" alt="{{ nextArticle.title }}" />
            </a>

            <a class="read__next-item-title"
              v-link="{ name: 'articleDetail', params: { articleId: nextArticle.id } }">
              {{ nextArticle.title }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        nextArticles: []
      }
    },

    ready: function () {
      this.$http(
        {
          url: '/api/articles/next/', method: 'GET'
        }
      ).then(function (response) {
        this.$set('nextArticles', response.data)
      }, function (response) {
        console.log(response)
      })
    }
  }
</script>
