# EMA Hourly Continuation — CARV/USDT P21_200

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.5990 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8058 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -3.3525 |
| sortino_ratio | -0.9875 |
| max_drawdown | 0.6355 |
| cagr | -0.3663 |
| net_avg_win | 58.1739 |
| net_avg_loss | -77.1920 |
| avg_hold_time_bars | 29.5571 |
| exposure | 0.5822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
