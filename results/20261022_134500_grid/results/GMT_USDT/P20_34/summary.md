# EMA Hourly Continuation — GMT/USDT P20_34

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.3552 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -11.2422 |
| sortino_ratio | -5.5006 |
| max_drawdown | 0.9991 |
| cagr | -0.9371 |
| net_avg_win | 11.6092 |
| net_avg_loss | -22.2284 |
| avg_hold_time_bars | 2.6106 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
