# EMA Hourly Continuation — AVAX/USDT P12_50

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.5325 |
| sortino_ratio | -0.8696 |
| max_drawdown | 0.6800 |
| cagr | -0.3296 |
| net_avg_win | 68.9789 |
| net_avg_loss | -85.5595 |
| avg_hold_time_bars | 11.5329 |
| exposure | 0.3030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
