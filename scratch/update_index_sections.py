import os

def update_index_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace projects background image with competitions image (images/IMG_7617.png)
    old_projects_bg = "<div class=\"stack-bg\" style=\"background-image: url('images/products-bg.png');\"></div>"
    new_projects_bg = "<div class=\"stack-bg\" style=\"background-image: url('images/IMG_7617.png');\"></div>"

    if old_projects_bg in content:
        content = content.replace(old_projects_bg, new_projects_bg, 1)

    # Remove the entire Competitions block
    # Pattern matching from Competitions comment to right before ABOUT US
    comp_block_1 = """    <!-- COMPETITIONS -->
    <div class="stack-block fade-in" id="competitions">
      <div class="stack-bg" style="background-image: url('images/IMG_7617.png');"></div>
      <div class="stack-overlay"></div>
      <div class="stack-content">
        <h3>Competitions</h3>
        <ul>
          <li>ICTMTC</li>
        </ul>
      </div>
    </div>\n\n"""

    comp_block_2 = """    <!-- COMPETITIONS -->
    <div class="stack-block fade-in" id="competitions">
      <div class="stack-bg" style="background-image: url('images/IMG_7617.png');"></div>
      <div class="stack-overlay"></div>
      <div class="stack-content">
        <h3>Competitions</h3>
        <ul>
          <li>ICTMTC</li>
        </ul>
      </div>
    </div>\r\n\r\n"""

    if comp_block_1 in content:
        content = content.replace(comp_block_1, "")
    elif comp_block_2 in content:
        content = content.replace(comp_block_2, "")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated {file_path}!")

def main():
    update_index_file('c:/Users/abdel/Desktop/aeris-website-main/index.html')
    update_index_file('c:/Users/abdel/Desktop/aeris-website-main/aeris-website-main/index.html')

if __name__ == '__main__':
    main()
