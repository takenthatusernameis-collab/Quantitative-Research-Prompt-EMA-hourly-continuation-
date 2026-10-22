# EMA Hourly Continuation — LQTY/USDT P12_34

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.7244 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9789 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.7308 |
| sortino_ratio | -1.0526 |
| max_drawdown | 0.7039 |
| cagr | -0.3824 |
| net_avg_win | 51.2255 |
| net_avg_loss | -69.9382 |
| avg_hold_time_bars | 7.3361 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
