<template>

  <header class="intro"
    v-if="randomArticle.id">
    <div class="intro__image"
      v-bind:style="hero_style">
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-12">
          <div class="post">
            <h1 class="post-title">
              <a v-link="{ name: 'articleDetail', params: { articleId: randomArticle.id } }">
                {{ randomArticle.title }}
              </a>
            </h1>

            <p class="post-meta">
              Posted by <a href="#">{{ randomArticle.author }}</a> on {{ randomArticle.publication_date }}
            </p>

            <div class="post-body">
              <p>
                {{{ randomArticle.body_text|truncatewords_html 100|linebreaks }}}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
        <div class="post" v-for="article in articles">
          <h2 class="post-title">
            <a v-link="{ name: 'articleDetail', params: { articleId: article.id } }">
              {{ article.title }}
            </a>
          </h2>
          <p class="post-meta">
            Posted by <a href="#">{{ article.author }}</a> on {{ article.publication_date }}</p>

          <div class="post-body">
            <p>
              {{{ article.body_text|truncatewords_html 50|linebreaks }}}
            </p>
          </div>

          <hr>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        randomArticle: {},
        articles: []
      }
    },

    ready: function () {
      this.$http(
        {
          url: '/api/articles/random/', method: 'GET'
        }
      ).then(function (response) {
        this.$set('randomArticle', response.data)
      }, function (response) {
        console.log(response)
      })

      this.$http(
        {
          url: '/api/articles/', method: 'GET'
        }
      ).then(function (response) {
        this.$set('articles', response.data)
      }, function (response) {
        console.log(response)
      })
    },

    computed: {
      hero_style: function () {
        return {
          backgroundImage: 'url(\'' + this.randomArticle.hero_image + '\')'
        }
      }
    }
  }
</script>
