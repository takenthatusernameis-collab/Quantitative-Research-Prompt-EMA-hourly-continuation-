# EMA Hourly Continuation — BIGTIME/USDT P20_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -2.6220 |
| sortino_ratio | -0.7949 |
| max_drawdown | 0.6133 |
| cagr | -0.3031 |
| net_avg_win | 52.9182 |
| net_avg_loss | -78.4377 |
| avg_hold_time_bars | 5.5312 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
