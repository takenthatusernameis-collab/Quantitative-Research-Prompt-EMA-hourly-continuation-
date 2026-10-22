# EMA Hourly Continuation — XDC/USDT P50_144

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.3191 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7491 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -6.7948 |
| sortino_ratio | -2.3483 |
| max_drawdown | 0.9530 |
| cagr | -0.7007 |
| net_avg_win | 16.9536 |
| net_avg_loss | -40.8631 |
| avg_hold_time_bars | 8.9636 |
| exposure | 0.2465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
