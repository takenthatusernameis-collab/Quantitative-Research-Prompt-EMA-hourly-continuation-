# EMA Hourly Continuation — PROM/USDT P12_50

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -3.9567 |
| sortino_ratio | -1.4613 |
| max_drawdown | 0.8202 |
| cagr | -0.4925 |
| net_avg_win | 51.0832 |
| net_avg_loss | -64.9812 |
| avg_hold_time_bars | 11.4645 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
