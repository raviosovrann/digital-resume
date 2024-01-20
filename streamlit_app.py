import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests


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
    
    # Load lottie files 
    def load_lottie_animation(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    # Animation data
    animation_1 = load_lottie_animation('https://lottie.host/22002488-7f65-4420-8e8b-47115ef50dce/JdMtyZ7Jr2.json')
    animation_2 = load_lottie_animation('https://lottie.host/728da99b-ae72-43b2-856c-292d4245c04c/uhgkxqXby6.json')
    animation_3 = load_lottie_animation('https://lottie.host/5cd3e33b-ecf8-48b5-bac8-fbd9121d4e27/ibUGY7pWi2.json')
    animation_4 = load_lottie_animation('https://lottie.host/73bfc708-f0fb-4514-9d8e-2f34357c9017/Hg9jvMHGXu.json')
    
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
        info_column, animation_column = st.columns((1, 1))
        with info_column:
            st.header("Hi, I am Anvar :wave:")
            st.write('')
            st.image(img)
            st.write(f"""
                    <div style="display: flex; margin-bottom: 20px;">
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
            st_lottie(animation_source=animation_1, speed=1, quality='high', height=500, width=600)
    st.divider()
        
    # Experience
    with st.container():
        st.header("Experience")
        left_col, middle_col, right_col = st.columns(3)
        with left_col:
            st.write('QA Analyst at DASH Financial Technologies', unsafe_allow_html=True)
            st.text('Jersey City, NJ')
            st.text('03/2022 – Present')
            st.info('''
                    -	Perform Smoke, Functional, Integration and Regression Testing in UAT and DEV environments
                    -	Develop and execute test plans, test cases and test scripts to ensure the quality of Software and Web Platform
                    -	Identified, documented, and reported software bugs via Jira, worked closely with Dev team to resolve them
                    -	Automated test cases using Python reducing testing time drastically and improving overall efficiency 
                    -	Collaborated with cross-function teams to ensure the successful deployment of new features and updates
                    -	Participated in Agile meetings such as: sprint planning, daily stand ups and weekly reviews
                     ''')
        with middle_col:
            st.write('Data Analyst at SCOUTFY', unsafe_allow_html=True)
            st.text('São Paulo, Brazil')
            st.text('04/2021 – 03/2022')
            st.info('''
                    -	Data mining through the collection of data of the world sports ecosystem
                    
                    -	Web Scraping with Selenium, Beautiful Soup, Scrapy to extract information from Web App UI
                    
                    -	Data Extraction from Web and Cloud systems (ETL)
                    
                    -	Data Transformation, removal of duplicates and Null values from data
                    
                    -  	Data Loading into CSV and JSON file formats
                    ''')
        with right_col:
            st.write('Internship at Boston Consulting Group', unsafe_allow_html=True)
            st.text('Virtual Internship')
            st.text('12/2019 – 03/2021')
            st.info('''
                    -	Fundamental understanding between the types of markets in which investments are traded.
                    
                    -	Differentiate different US regulatory agencies for stock market
                    
                    -	Understand the difference between the various types of brokerage offerings.
                    
                    -	Understand municipal bonds to corporate bonds as investment options
                    
                    -	Arbitrage in the foreign exchange market
                    
                    -	Understanding of the factors involved in commodities pricing.
                    ''')
    st.divider()
    
    # Tech Stack
    with st.container():
        st.header('Tech Stack')
        stack_animation, info = st.columns((1, 1))
        with stack_animation:
            st_lottie(animation_source=animation_2, speed=1, quality='high', height=300, width=600)
        with info:
            st.write('''
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
                    ''', unsafe_allow_html=True)
        st.divider()
    
    # Certifications
    with st.container():
        st.header('Certifications')
        cert_animation, certs = st.columns((1, 1))
        with cert_animation:
            st_lottie(animation_source=animation_3, speed=1, quality='high', height=300, width=600)
        with certs:
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('''
                     - Google - Crash Course on Python: {url1}
                     
                     - Google - Using Python to Interact with OS: {url2}
                     
                     - Google - Introduction to Git and Github: {url3}
                     
                     - Google - Troubleshooting and Debugging Techniques: {url4}
                     
                     '''.format(url1='https://rb.gy/f9qlhs', url2='https://shorturl.at/aoxR6', url3='https://rb.gy/36m2b5', url4='https://shorturl.at/dnpxH'))
    st.divider()
    
    # Education
    with st.container():
        st.header('Education')
        education, edu_animation = st.columns((1, 1))
        with education:
            st.write('##')
            st.write('##')
            st.write('##')
            st.write('''
                     
                     * CUNY Hunter College – Computer Science (2017 – 2021)
                     
                     * CUNY Baruch College – Data Analysis (2023 – present)
                     
                     ''')
        with edu_animation:
            st_lottie(animation_source=animation_4, speed=1, quality='high', height=300, width=600) 


if __name__ == "__main__":
    main()
