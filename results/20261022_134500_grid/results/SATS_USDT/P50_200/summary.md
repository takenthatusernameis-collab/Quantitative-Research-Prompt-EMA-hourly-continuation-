# EMA Hourly Continuation — SATS/USDT P50_200

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.5735 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.7885 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -3.1496 |
| sortino_ratio | -0.8663 |
| max_drawdown | 0.6474 |
| cagr | -0.3326 |
| net_avg_win | 51.1857 |
| net_avg_loss | -70.0626 |
| avg_hold_time_bars | 20.4686 |
| exposure | 0.3538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
