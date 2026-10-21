# EMA Hourly Continuation — LISTA/USDT P21_50

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -3.7168 |
| sortino_ratio | -1.2622 |
| max_drawdown | 0.7416 |
| cagr | -0.4399 |
| net_avg_win | 47.3260 |
| net_avg_loss | -62.7859 |
| avg_hold_time_bars | 7.8233 |
| exposure | 0.2035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
