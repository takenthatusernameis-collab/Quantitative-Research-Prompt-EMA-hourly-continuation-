# EMA Hourly Continuation — ETHFI/USDT P55_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 1.0002 |
| net_win_rate | 0.5484 |
| gross_profit_factor | 1.2009 |
| gross_win_rate | 0.5484 |
| sharpe_ratio | 0.0598 |
| sortino_ratio | 0.0160 |
| max_drawdown | 0.1833 |
| cagr | 0.0002 |
| net_avg_win | 98.4090 |
| net_avg_loss | -119.4669 |
| avg_hold_time_bars | 15.4751 |
| exposure | 0.2399 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
