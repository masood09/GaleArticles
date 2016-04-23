<template>
  <header class="search">
    <div class="container">
      <div class="row">
        <div class="col-xs-8 col-xs-offset-2">
          <div class="input-group">
            <div class="input-group-btn search-panel">
              <input type="text" id="article__search_input" class="form-control" name="q" value="{{ term }}" placeholder="Enter your search term and hit enter..." v-on:keyup.enter="searchSubmit($event)">
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <hr>

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
  import jQuery from 'jquery'

  export default {
    data () {
      return {
        articles: []
      }
    },

    methods: {
      searchSubmit: function (event) {
        event.preventDefault()

        var _searchTerm = jQuery('#article__search_input').val()

        if (_searchTerm) {
          this.$http({
            url: '/api/articles/search/',
            method: 'GET',
            params: {q: _searchTerm}
          }).then(function (response) {
            this.$set('articles', response.data)
          }, function (response) {
            console.log(response)
          })
        }
      }
    }
  }
</script>
