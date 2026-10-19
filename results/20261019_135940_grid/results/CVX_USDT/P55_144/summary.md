# EMA Hourly Continuation — CVX/USDT P55_144

**Symbol:** CVX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5349 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.7975 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -4.0034 |
| sortino_ratio | -1.2213 |
| max_drawdown | 0.7703 |
| cagr | -0.4433 |
| net_avg_win | 42.8051 |
| net_avg_loss | -62.7419 |
| avg_hold_time_bars | 11.2059 |
| exposure | 0.2399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
