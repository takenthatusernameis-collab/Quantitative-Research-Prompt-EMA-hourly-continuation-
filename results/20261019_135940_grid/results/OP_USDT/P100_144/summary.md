# EMA Hourly Continuation — OP/USDT P100_144

**Symbol:** OP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.4979 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -5.1526 |
| sortino_ratio | -1.6613 |
| max_drawdown | 0.8636 |
| cagr | -0.5476 |
| net_avg_win | 37.3892 |
| net_avg_loss | -60.7692 |
| avg_hold_time_bars | 3.6543 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
