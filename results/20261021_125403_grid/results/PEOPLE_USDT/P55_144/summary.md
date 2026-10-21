# EMA Hourly Continuation — PEOPLE/USDT P55_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -1.4978 |
| sortino_ratio | -0.4070 |
| max_drawdown | 0.4366 |
| cagr | -0.1710 |
| net_avg_win | 69.0317 |
| net_avg_loss | -87.1713 |
| avg_hold_time_bars | 16.9753 |
| exposure | 0.2796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
