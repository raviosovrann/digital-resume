import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

# Loading JSON file 
def load_lottie_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
        
def main():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Anvar's Digital Resume",
        page_icon="📍",
        layout='wide'
    )
    
    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # PDF CV file
    with open("assets/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        
    # Profile image file
    img = Image.open('assets/profile.png')

    
    # Animation data
    animation_1 = load_lottie_json('assets/Animation - 1705722032566.json')
    animation_2 = load_lottie_json('assets/Animation - 1705722884068.json')
    animation_3 = load_lottie_json('assets/Animation - 1705725358517.json')
    animation_4 = load_lottie_json('assets/Animation - 1705726809165.json')
    
    
    # Social links dictionary     
    socials = {
        # Platform [URL, Icon]
        'LinkedIn': ['https://www.linkedin.com/in/anvarnosirov/','https://cdn-icons-png.flaticon.com/512/174/174857.png'],
        'Github': ['https://github.com/raviosovrann','https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg'],
        'YouTube': ['https://www.youtube.com/channel/UCXHIjJ6iCOhJIiwYCS0-PHw','https://cdn-icons-png.flaticon.com/512/1384/1384060.png']
    }
    
    socials_html = [f"<a href='{socials[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{socials[platform][1]}' alt='{platform}'></a>" for platform in socials]
    
    
    # Title profile image and social icons
    with st.container():
        info_column, animation_column = st.columns((1, 3))
        with info_column:
            st.header("Hi, I am Anvar :wave:")
            st.write('')
            st.image(img)
            st.write(f"""
                    <div style="display: flex; margin-bottom: 15px;">
                        {''.join(socials_html)}
                    </div>""", 
                    unsafe_allow_html=True)
            st.subheader("QA Analyst From NYC")
            st.write('''
                     Contact Information: anvar.nosirov07@gmail.com 
                     ''', unsafe_allow_html=True)
            
            # Download CV button
            st.download_button(
                label="📄 Download my Resume",
                data=pdf_bytes,
                file_name="Resume.pdf",
                mime="application/pdf",
            )
            
        with animation_column:
            st_lottie(animation_source=animation_1, speed=1, quality='high', height=400, width=400)
    st.divider()
        
    # Experience
    with st.container():
        st.header("Experience")
        st.write('')
        
        st.subheader('_QA Analyst at DASH Financial Technologies | Jersey City, NJ_')
        st.caption('_03/2022 – Present_')
        st.info('_DASH Financial Technologies is a leading trading technology provider that offers customizable solutions to help clients grow and maximize revenue_')
        st.text('''
                - Led comprehensive testing (Smoke, Functional, Integration, Regression) in UAT and DEV environments to fortify software quality.
                
                - Developed and executed test plans, cases, and scripts, identifying, and resolving software bugs with precision.
                
                - Automated test cases with Python, reducing testing time by 35% and enhancing overall efficiency.
                
                - Collaborated cross-functionally, ensuring seamless deployment of new features and updates, streamlining development.
                
                - Proficient in Agile methodology, delivering exemplary client support, and conducting efficient database and server testing.
                    ''')
        st.write('###')
        
    with st.container():
        st.subheader('_Data Analyst at SCOUTFY | São Paulo, Brazil_')
        st.caption('_04/2021 – 03/2022_')
        st.info('_SCOUTFY is a company that provides innovative and efficient solutions for the sportscience industry, focusing on collecting and optimizing athlete data_')
        st.text('''
                - Conducted extensive data mining within the global sports ecosystem, strategically collecting pertinent data for analysis.
                
                - Applied advanced web scraping techniques using Selenium, Beautiful Soup, and Scrapy to extract valuable information from Web App UI.
                
                - Proficiently performed Data Extraction from Web and Cloud systems using ETL (Extract, Transform, Load) processes.
                
                - Implemented meticulous Data Transformation techniques, including the removal of duplicates and null values, to ensure data integrity and accuracy.
                
                - Executed seamless data loading into CSV and JSON file formats, facilitating efficient data storage and retrieval processes.
                ''')
        st.write('###')
        
    with st.container():
        st.subheader('_Internship at Boston Consulting Group | Virtual Internship_')
        st.caption('_12/2019 – 03/2021_')
        st.info('_Boston Consulting Group (BCG) is a global management consulting firm that partners with leaders in business and society to tackle any financial challenges_')
        st.text('''
                - Demonstrated a profound comprehension of the diverse markets in which investments are traded, discerning key nuances between various market types.
                
                - Distinguished and comprehensively understood the regulatory frameworks set forth by different US regulatory agencies governing the stock market.
                
                - Exhibited an in-depth understanding of the distinct offerings provided by various brokerage entities, showcasing expertise in brokerage services.
                
                - Leveraged knowledge to differentiate between municipal bonds and corporate bonds, presenting insightful investment options to stakeholders.
                
                - Applied strategic insight to navigate arbitrage opportunities in the foreign exchange market, contributing to effective financial optimization.
                
                - Displayed analytical acumen in comprehending the multifaceted factors influencing commodities pricing, enhancing investment landscape.
                ''')
    st.divider()
    
    # Tech Stack
    with st.container():
        st.header('Tech Stack')
        stack_animation, info = st.columns((1, 3))
        with stack_animation:
            st_lottie(animation_source=animation_2, speed=1, quality='high', height=400, width=300)
        with info:
            st.text('''
                        - Python / Django / Flask / Streamlit / Flask
                        - Mac OS / Windows / Linux
                        - Jira / Confluence / Zephyr
                        - Selenium / Playwright / PyTest
                        - HTML / CSS / JS
                        - Git / Github / Jenkins
                        - XML / YAML / TOML
                        - TestRail
                        - SQL
                        - FIX Protocol
                        - Microsoft Office Suite 
                        - Postman
                    ''')
        st.divider()
    
    # Certifications
    with st.container():
        st.header('Certifications')
        cert_animation, certs = st.columns((1, 3))
        with cert_animation:
            st_lottie(animation_source=animation_3, speed=1, quality='high', height=400, width=300)
        with certs:
            st.text('''
                     - Google - Crash Course on Python: {url1}
                     
                     - Google - Using Python to Interact with OS: {url2}
                     
                     - Google - Introduction to Git and Github: {url3}
                     
                     - Google - Troubleshooting and Debugging Techniques: {url4}
                     
                     '''.format(url1='https://rb.gy/f9qlhs', url2='https://shorturl.at/aoxR6', url3='https://rb.gy/36m2b5', url4='https://shorturl.at/dnpxH'))
    st.divider()
    
    # Education
    with st.container():
        st.header('Education')
        edu_animation, education = st.columns((1, 3))
        with edu_animation:
            st_lottie(animation_source=animation_4, quality='high', height=400, width=300) 
        with education:
            st.text('''
                     
                     - CUNY Hunter College – Computer Science (2017 – 2021)
                     
                     - CUNY Baruch College – CyberSecurity (2023 – present)
                     
                     ''')


if __name__ == "__main__":
    main()
