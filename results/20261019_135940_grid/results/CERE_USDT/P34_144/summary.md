# EMA Hourly Continuation — CERE/USDT P34_144

**Symbol:** CERE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4948 |
| net_win_rate | 0.3508 |
| gross_profit_factor | 0.7700 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -8.1750 |
| sortino_ratio | -2.8042 |
| max_drawdown | 0.9771 |
| cagr | -0.7662 |
| net_avg_win | 46.0916 |
| net_avg_loss | -50.3416 |
| avg_hold_time_bars | 14.7678 |
| exposure | 0.3960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
