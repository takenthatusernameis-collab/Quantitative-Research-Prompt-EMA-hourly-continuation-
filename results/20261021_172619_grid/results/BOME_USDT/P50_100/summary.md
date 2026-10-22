# EMA Hourly Continuation — BOME/USDT P50_100

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0595 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -0.8496 |
| sortino_ratio | -0.2359 |
| max_drawdown | 0.2873 |
| cagr | -0.1052 |
| net_avg_win | 74.5430 |
| net_avg_loss | -93.9808 |
| avg_hold_time_bars | 9.4785 |
| exposure | 0.1603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
