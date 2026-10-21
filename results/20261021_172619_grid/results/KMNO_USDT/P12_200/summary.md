# EMA Hourly Continuation — KMNO/USDT P12_200

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.8262 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.0705 |
| sortino_ratio | -0.2631 |
| max_drawdown | 0.3318 |
| cagr | -0.1162 |
| net_avg_win | 86.8790 |
| net_avg_loss | -101.6202 |
| avg_hold_time_bars | 53.5973 |
| exposure | 0.7251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
