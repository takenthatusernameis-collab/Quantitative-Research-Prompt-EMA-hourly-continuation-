# EMA Hourly Continuation — POPCAT/USDT P89_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.8611 |
| net_win_rate | 0.5424 |
| gross_profit_factor | 1.1712 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | -0.5100 |
| sortino_ratio | -0.0863 |
| max_drawdown | 0.1179 |
| cagr | -0.0399 |
| net_avg_win | 81.5722 |
| net_avg_loss | -112.2754 |
| avg_hold_time_bars | 4.7627 |
| exposure | 0.0297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
