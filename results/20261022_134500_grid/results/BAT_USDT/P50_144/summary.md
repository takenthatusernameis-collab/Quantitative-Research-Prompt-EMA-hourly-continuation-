# EMA Hourly Continuation — BAT/USDT P50_144

**Symbol:** BAT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8413 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -4.4982 |
| sortino_ratio | -1.4347 |
| max_drawdown | 0.8250 |
| cagr | -0.4959 |
| net_avg_win | 37.6407 |
| net_avg_loss | -59.6801 |
| avg_hold_time_bars | 10.4697 |
| exposure | 0.2432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
