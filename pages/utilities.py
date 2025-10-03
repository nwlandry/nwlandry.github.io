import yaml
from IPython.display import HTML, Markdown, display


def readable_list(_s):
    if len(_s) < 3:
        return " and ".join(map(str, _s))
    *a, b = _s
    return f"{', '.join(map(str, a))}, and {b}"


def button(url, str, icon):
    icon_base = icon[:2]
    return f"""<a class="btn btn-outline-dark btn-sm", href="{url}" target="_blank" rel="noopener noreferrer">
        <i class="{icon_base} {icon}" role='img' aria-label='{str}'></i>
        {str}
    </a>"""


def load_publication_data(path):
    yaml_data = yaml.safe_load(open(path))
    pub_strs = {"pubs": {}, "wps": {}, "theses": {}}
    for _, data in yaml_data.items():
        title_str = data["title"]
        authors = data.get("authors", ["me"])
        authors = [
            a if a != "NWL" else "<strong>Nicholas W. Landry</strong>" for a in authors
        ]
        author_str = readable_list(authors)
        year_str = data["year"]

        buttons = []
        pdf = data.get("pdf")
        if pdf is not None:
            buttons.append(button(pdf, "PDF", "bi-file-earmark-pdf"))

        preprint = data.get("preprint")
        if preprint is not None:
            buttons.append(button(preprint, "Preprint", "ai-arxiv"))

        code = data.get("code")
        if code is not None:
            buttons.append(button(code, "Code", "bi-github"))

        pub_url = data.get("published_url")
        venue = data.get("venue")
        thesis_type = data.get("thesis")

        pub_str = f'{author_str}, "{title_str}",'

        if venue is not None:
            pub_str += f" <em>{venue}</em>"

        if thesis_type is not None:
            pub_str += f", <em>{thesis_type} Thesis</em>"

        pub_str += f" ({year_str})."

        if pub_url is None:
            if year_str not in pub_strs["wps"]:
                pub_strs["wps"][year_str] = []
            pub_strs["wps"][year_str].append(
                "<li class='list-group-item border-0'>"
                + pub_str
                + "<br>"
                + " ".join(buttons)
                + "</li>"
            )
        elif thesis_type is not None:
            if year_str not in pub_strs["theses"]:
                pub_strs["theses"][year_str] = []
            buttons.append(button(pub_url, "Published", "ai-archive"))
            pub_strs["theses"][year_str].append(
                "<li class='list-group-item border-0'>"
                + pub_str
                + "<br>"
                + " ".join(buttons)
                + "</li>"
            )
        else:
            if year_str not in pub_strs["pubs"]:
                pub_strs["pubs"][year_str] = []
            buttons.append(button(pub_url, "Published", "ai-archive"))
            pub_strs["pubs"][year_str].append(
                "<li class='list-group-item border-0'>"
                + pub_str
                + "<br>"
                + " ".join(buttons)
                + "</li>"
            )
    return pub_strs


def load_software_data(path):
    yaml_data = yaml.safe_load(open(path))
    for _, data in yaml_data.items():
        display(Markdown("## `" + data["title"] + "`"))
        display(Markdown(data["description"]))
        display(Markdown("(*" + data["role"] + "*)"))
        buttons = []
        if "website" in data:
            buttons.append(button(data["website"], "Website", "bi-info-circle"))
        if "github" in data:
            buttons.append(button(data["github"], "Github", "bi-github"))
        if "package" in data:
            buttons.append(button(data["package"], "Package", "bi-box-seam"))
        display(HTML(" ".join(buttons)))
    return
