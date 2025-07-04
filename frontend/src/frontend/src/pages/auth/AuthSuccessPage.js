import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import { CheckCircle, Loader } from "lucide-react";
import { getTokenFromUrl, getErrorFromUrl, cleanUrl } from "../../utils/auth";
import { useAppContext } from "../../contexts/AppContext";
import { useToast } from "../../hooks/useToast";
import apiService from "../../services/api";

const PageContainer = styled.div`
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(
    135deg,
    #f0fdfa 0%,
    #ffffff 35%,
    #f0f9ff 65%,
    #ecfdf5 100%
  );
`;

const Card = styled.div`
  background: white;
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 0 32px 64px -12px rgba(0, 0, 0, 0.08);
  text-align: center;
  max-width: 400px;
  width: 100%;
  margin: 1rem;
`;

const IconContainer = styled.div`
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981, #0891b2);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
`;

const Title = styled.h1`
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
`;

const Description = styled.p`
  color: #6b7280;
  font-size: 0.9rem;
  line-height: 1.5;
`;

const LoadingContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 1rem;
`;

const Spinner = styled(Loader)`
  animation: spin 1s linear infinite;

  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
`;

function AuthSuccessPage() {
  const navigate = useNavigate();
  const { setUser } = useAppContext();
  const { showToast } = useToast();

  useEffect(() => {
    const handleAuth = async () => {
      const token = getTokenFromUrl();
      const error = getErrorFromUrl();

      if (error) {
        showToast.error("로그인 중 오류가 발생했습니다.");
        navigate("/login");
        return;
      }

      if (token) {
        try {
          // 토큰 저장
          apiService.setToken(token);

          // 사용자 정보 가져오기
          const userProfile = await apiService.auth.getProfile();
          setUser(userProfile);

          showToast.success("로그인이 완료되었습니다!");

          // URL 정리 후 대시보드로 이동
          cleanUrl();
          navigate("/dashboard");
        } catch (error) {
          console.error("Authentication error:", error);
          showToast.error("사용자 정보를 가져오는데 실패했습니다.");
          navigate("/login");
        }
      } else {
        showToast.error("인증 토큰을 찾을 수 없습니다.");
        navigate("/login");
      }
    };

    handleAuth();
  }, [navigate, setUser, showToast]);

  return (
    <PageContainer>
      <Card>
        <IconContainer>
          <CheckCircle size={32} />
        </IconContainer>
        <Title>로그인 성공!</Title>
        <Description>
          계정 정보를 확인하고 있습니다.
          <br />
          잠시만 기다려주세요.
        </Description>
        <LoadingContainer>
          <Spinner size={20} />
          <span>처리 중...</span>
        </LoadingContainer>
      </Card>
    </PageContainer>
  );
}

export default AuthSuccessPage;
