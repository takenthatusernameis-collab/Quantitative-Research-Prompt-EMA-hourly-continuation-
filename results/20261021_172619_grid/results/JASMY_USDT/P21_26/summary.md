# EMA Hourly Continuation — JASMY/USDT P21_26

**Symbol:** JASMY/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 109 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8356 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -1.4991 |
| sortino_ratio | -0.2234 |
| max_drawdown | 0.2450 |
| cagr | -0.0975 |
| net_avg_win | 75.3243 |
| net_avg_loss | -102.3110 |
| avg_hold_time_bars | 3.8165 |
| exposure | 0.0189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
