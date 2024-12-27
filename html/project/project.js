document.addEventListener('DOMContentLoaded', () => {
    // 공통 기능: 현재 시간 표시
    const updateTime = () => {
        const now = new Date();
        const formattedTime = now.toLocaleTimeString('ko-KR', {
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
        });
        const currentTimeElement = document.getElementById('currentTime');
        if (currentTimeElement) {
            currentTimeElement.textContent = `${formattedTime}`;
        }
    };
    setInterval(updateTime, 1000);
    updateTime();

    // 공통 기능: 테마 설정
    const setTheme = (theme) => {
        document.documentElement.setAttribute('data-bs-theme', theme);
        localStorage.setItem('theme', theme);
    };

    const storedTheme = localStorage.getItem('theme') || 'auto';
    setTheme(storedTheme);

    const lightThemeButton = document.getElementById('lightTheme');
    const darkThemeButton = document.getElementById('darkTheme');

    if (lightThemeButton) {
        lightThemeButton.addEventListener('click', () => setTheme('light'));
    }

    if (darkThemeButton) {
        darkThemeButton.addEventListener('click', () => setTheme('dark'));
    }

    // 페이지별 추가 기능
    const productTable = document.getElementById('product_data_Table');
    if (productTable) {
        // index.html에서만 작동
        const product_data = [
            { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
            { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
            { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
            { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
        ];

        product_data.forEach((item) => {
            const row = productTable.insertRow();
            row.insertCell(0).innerHTML = item.category;
            row.insertCell(1).innerHTML = item.brand;
            row.insertCell(2).innerHTML = item.product;
            row.insertCell(3).innerHTML = item.price;
        });
    }
});
