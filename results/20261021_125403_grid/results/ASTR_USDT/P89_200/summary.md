# EMA Hourly Continuation — ASTR/USDT P89_200

**Symbol:** ASTR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7317 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.6844 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.4300 |
| cagr | -0.1753 |
| net_avg_win | 69.9973 |
| net_avg_loss | -95.0324 |
| avg_hold_time_bars | 16.7342 |
| exposure | 0.2279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
