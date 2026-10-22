# EMA Hourly Continuation — STRK/USDT P89_200

**Symbol:** STRK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -2.1169 |
| sortino_ratio | -0.5887 |
| max_drawdown | 0.5414 |
| cagr | -0.2436 |
| net_avg_win | 64.9314 |
| net_avg_loss | -89.7808 |
| avg_hold_time_bars | 12.2481 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
