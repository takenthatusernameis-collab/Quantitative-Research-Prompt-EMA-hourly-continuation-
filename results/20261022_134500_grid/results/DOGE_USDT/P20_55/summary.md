# EMA Hourly Continuation — DOGE/USDT P20_55

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.4377 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -7.8463 |
| sortino_ratio | -3.3139 |
| max_drawdown | 0.9853 |
| cagr | -0.8132 |
| net_avg_win | 19.2228 |
| net_avg_loss | -34.2223 |
| avg_hold_time_bars | 5.8968 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
