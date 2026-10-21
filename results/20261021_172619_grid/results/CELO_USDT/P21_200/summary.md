# EMA Hourly Continuation — CELO/USDT P21_200

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8615 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0251 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.8611 |
| sortino_ratio | -0.2137 |
| max_drawdown | 0.3336 |
| cagr | -0.0959 |
| net_avg_win | 91.9449 |
| net_avg_loss | -108.1440 |
| avg_hold_time_bars | 46.0960 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
