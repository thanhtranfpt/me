class FilesHandler:
    def __init__(self) -> None:
        pass

class Logger:
    def __init__(self) -> None:
        """
        Note: in logging_utils.py
        """
        pass

class Docker:
    def __init__(self) -> None:
        """
        Note:

        ===================== DOCKER ========================

        sudo docker-compose up --build : để build
        --> sửa file xong là phải build lại.

        docker-compose up : để chạy

        docker-compose down : để đóng docker container.

        xóa image: docker rmi IMAGE_ID : 3 chữ cái đầu.

        xem các docker images nào đã xây dựng: docker images

        xem logs: docker-compose logs camera_service --tail=50

        CMD là phải nháy kép, command trong docker-compose.yaml có thể nháy đơn. command này sẽ ghi đè CMD.

        ===========================================================================

        """
        """
        ================= để sử dụng flask app trong docker ==================
        app.config['HOST'] = '0.0.0.0'
        app.config['PORT'] = 8080

        if __name__ == '__main__':
            app.run(host=app.config['HOST'], port=app.config['PORT'])

        docker build -t my-flask-app .
        docker run -p 8080:8080 my-flask-app

        ===========================================================================

        """
        """
        ===========================================================================
        =============== xem redisedge trong docker từ bên ngoài ============
        localhost:6379
        ===========================================================================
        """
        pass

class RequirementsFileHandler:
    def __init__(self) -> None:
        """
        Note:
        ĐỂ KIỂM TRA 1 package có phải module hay không để bỏ vào file requirements.txt, kiểm tra tại:
        https://docs.python.org/3/library/index.html
        """
        pass

class Yolov8Handler:
    def __init__(self) -> None:
        pass
    def to_gpu(self):
        """
        Note:
        ======= MODEL TO GPU ==========
        model = YOLO().to("cuda")
        """
        pass