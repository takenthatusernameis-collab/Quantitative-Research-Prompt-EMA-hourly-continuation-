# EMA Hourly Continuation — MINA/USDT P8_50

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.6319 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -5.0272 |
| sortino_ratio | -2.2177 |
| max_drawdown | 0.9347 |
| cagr | -0.6545 |
| net_avg_win | 33.9993 |
| net_avg_loss | -49.3877 |
| avg_hold_time_bars | 11.5295 |
| exposure | 0.5146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
