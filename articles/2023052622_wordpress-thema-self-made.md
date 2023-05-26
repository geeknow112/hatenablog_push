WordPress初心者でもできる！簡単テーマ自作入門
wordpress,thema,自作,php
wordpress-thema-self-made

# はじめに
こんにちは。今回は、WordPress初心者に向けて、テーマ自作の入門方法をご紹介します。WordPressを使ってウェブサイトを作成する際、テーマはとても重要な要素です。しかし、既存のテーマではなかなか理想のデザインにならない場合もあります。そんな時は、自分でテーマを作ってみましょう！初心者でも簡単にテーマ自作ができる方法を解説します。

## テーマ自作の前提条件

テーマ自作には、以下の前提条件が必要です。

- HTML/CSSの基本的な知識
- WordPressの基本的な操作方法の理解
- テキストエディタの使用経験

これらの基本的な知識があれば、テーマ自作に取り組むことができます。

## テーマ自作の手順

### 1. テーマフォルダの作成

まずは、テーマフォルダを作成します。WordPressのテーマは、`wp-content/themes/`の中に保存されます。例えば、`wp-content/themes/mytheme/`のようにフォルダを作成します。ここで、`mytheme`は任意の名前です。

### 2. style.cssの作成

次に、テーマのスタイルを定義する`style.css`を作成します。以下のように、テーマの名前や説明を記述します。

```
/*
Theme Name: My Theme
Theme URI: https://example.com/
Description: My first WordPress theme.
Author: Your Name
Author URI: https://example.com/
Version: 1.0
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: blog, custom-background, custom-header, custom-menu, featured-images, flexible-header, post-formats, rtl-language-support, sticky-post, threaded-comments, translation-ready
*/
```

### 3. index.phpの作成

次に、テーマのメインテンプレートである`index.php`を作成します。`index.php`は、WordPressのテンプレート階層の最上位に位置し、テーマの基本的な構造を定義します。以下は、基本的な`index.php`の構造です。

```
<?php get_header(); ?>

<main id="main" class="site-main">

  <?php if ( have_posts() ) : ?>

    <?php while ( have_posts() ) : the_post(); ?>

      <?php get_template_part( 'template-parts/content', get_post_format() ); ?>

    <?php endwhile; ?>

  <?php endif; ?>

</main><!-- #main -->

<?php get_footer(); ?>
```

### 4. header.phpとfooter.phpの作成

次に、テーマのヘッダーとフッターを定義する`header.php`と`footer.php`を作成します。以下は、基本的な`header.php`と`footer.php`の構造です。

`header.php`:

```
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo( 'charset' ); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
  <header id="masthead" class="site-header">
    <div class="site-branding">
      <h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
      <p class="site-description"><?php bloginfo( 'description' ); ?></p>
    </div><!-- .site-branding -->
    <nav id="site-navigation" class="main-navigation">
      <?php wp_nav_menu( array( 'theme_location' => 'primary', 'menu_id' => 'primary-menu' ) ); ?>
    </nav><!-- #site-navigation -->
  </header><!-- #masthead -->
```

`footer.php`:

```
<footer id="colophon" class="site-footer">
  <div class="site-info">
    <?php
      printf( esc_html__( 'Copyright © %1$s %2$s', 'mytheme' ), 
        date( 'Y' ), 
        esc_html( get_bloginfo( 'name' ) ) 
      );
    ?>
  </div><!-- .site-info -->
</footer><!-- #colophon -->
<?php wp_footer(); ?>
</body>
</html>
```

### 5. テンプレートファイルの作成

最後に、テンプレートファイルを作成します。テンプレートファイルは、テーマのデザインを定義するファイルで、`index.php`以外のページに対して、異なるデザインを適用することができます。以下は、基本的なテンプレートファイルの構造です。

- `archive.php`: 投稿の一覧ページに対するテンプレート
- `single.php`: 投稿の個別ページに対するテンプレート
- `page.php`: 固定ページに対するテンプレート
- `404.php`: 404エラーページに対するテンプレート

テンプレートファイルを作成する際には、WordPressのテンプレートタグやループ構文を使用して、テーマのデザインを自由にカスタマイズすることができます。

## まとめ

以上が、WordPress初心者でも簡単にテーマ自作ができる手順です。テーマ自作には、HTML/CSSの基本的な知識と、WordPressの基本的な操作方法が必要ですが、これらを理解していれば誰でも挑戦できます。自分だけのデザインを実現し、オリジナリティあふれるウェブサイトを作成しましょう！

