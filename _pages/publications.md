---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

{% include base_path %}

You can also find my articles on <a href="https://scholar.google.com/citations?user=jucvWbcAAAAJ&hl=en" target="_blank" rel="noopener">my Google Scholar profile</a>. *Names marked with an asterisk denote equal contribution.*

<div class="archive-list" style="margin-top: 2rem;">
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</div>
