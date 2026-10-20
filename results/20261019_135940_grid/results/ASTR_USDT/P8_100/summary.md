# EMA Hourly Continuation — ASTR/USDT P8_100

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9736 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -3.3097 |
| sortino_ratio | -1.1289 |
| max_drawdown | 0.7534 |
| cagr | -0.4149 |
| net_avg_win | 46.4050 |
| net_avg_loss | -67.6654 |
| avg_hold_time_bars | 25.6271 |
| exposure | 0.6842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
