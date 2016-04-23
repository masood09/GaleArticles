<template>
  <header class="intro"
    v-if="article.id">
    <div class="intro__image" v-bind:style="hero_style"></div>
  </header>

  <div class="container"
    v-if="article.id">
    <div class="row">
      <div class="col-sm-8">
        <div class="post">
          <h1 class="post-title">
            {{ article.title }}
          </h1>

          <p class="post-meta">
            Posted by <a href="#">{{ article.author }}</a> on {{ article.publication_date }}
          </p>

          <div class="post-body">
            <p>
              {{{ article.body_text|linebreaks }}}
            </p>
          </div>
        </div>
      </div>

      <div class="col-sm-4"
        v-if="article.optional_image">
        <div class="post">
          <img v-bind:src="article.optional_image" class="post-optional-image">
        </div>
      </div>
    </div>
  </div>

  <hr>
</template>

<script>
  export default {
    data () {
      return {
        article: {}
      }
    },

    ready: function () {
      this.$http(
        {
          url: '/api/articles/' + this.$route.params.articleId, method: 'GET'
        }
      ).then(function (response) {
        this.$set('article', response.data)
      }, function (response) {
        console.log(response)
      })
    },

    computed: {
      hero_style: function () {
        return {
          backgroundImage: 'url(\'' + this.article.hero_image + '\')'
        }
      }
    }
  }
</script>
