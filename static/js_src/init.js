$(document).ready(function(){
    //Navigation Menu Slider
    $('#nav-expander').on('click',function(e){
        e.preventDefault();
        $('body').toggleClass('nav-expanded');
    });

    $('#nav-close').on('click',function(e){
        e.preventDefault();
        $('body').removeClass('nav-expanded');
    });

    $('.slick__carousel').slick();
});

Vue.config.devtools = false;
Vue.config.delimiters = ['${', '}'];
Vue.config.unsafeDelimiters = ['{!!', '!!}'];

Vue.filter('trim_linebreaks', function(value) {
    value = value.replace(/(?:\r\n|\r|\n)/g, '<br>');

    return value.split(" ").splice(0, 50).join(" ");
});

article__search = {
    init: function() {
        new Vue({
            el: '#vue__container',

            data: {
                articles: []
            },
            
            ready: function() {
                _search_term = jQuery('#article__search_input').val();

                if (_search_term) {
                    this.$http({
                        url: jQuery('#api__article_search_url').val(),
                        method: 'GET',
                        params: {q: _search_term}
                    }).then(function (response) {
                        this.$set('articles', response.data)
                    }, function (response) {
                        console.log(response);
                    });
                }
            },

            methods: {
                searchSubmit: function (event) {
                    event.preventDefault();

                    _search_term = jQuery('#article__search_input').val();

                    if (_search_term) {
                        this.$http({
                            url: jQuery('#api__article_search_url').val(),
                            method: 'GET',
                            params: {q: _search_term}
                        }).then(function (response) {
                            this.$set('articles', response.data)
                        }, function (response) {
                            console.log(response);
                        });
                    }
                }
            }
        });
    }
};

article__detail = {
    init: function() {
        new Vue({
            el: '#vue__container',

            data: {
                article: []
            },

            ready: function() {
                this.$http({url: jQuery('#api__article_detail_url').val(), method: 'GET'}).then(function (response) {
                    this.$set('article', response.data)
                }, function (response) {
                    console.log(response);
                });
            },

            computed: {
                body_text_linebreaks: function () {
                    return this.article.body_text.replace(/(?:\r\n|\r|\n)/g, '<br>');
                },

                hero_style: function() {
                    return {
                        backgroundImage: 'url(\'' + this.article.hero_image + '\')'
                    };
                }
            }
        });
    }
};
