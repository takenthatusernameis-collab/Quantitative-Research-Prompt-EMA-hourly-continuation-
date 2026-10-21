# EMA Hourly Continuation — SAFE/USDT P12_20

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.5030 |
| sortino_ratio | -0.6700 |
| max_drawdown | 0.5409 |
| cagr | -0.2631 |
| net_avg_win | 57.7647 |
| net_avg_loss | -83.1899 |
| avg_hold_time_bars | 7.2478 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
