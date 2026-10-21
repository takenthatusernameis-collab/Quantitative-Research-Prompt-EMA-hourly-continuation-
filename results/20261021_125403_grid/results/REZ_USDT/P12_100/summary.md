# EMA Hourly Continuation — REZ/USDT P12_100

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.9747 |
| net_win_rate | 0.5366 |
| gross_profit_factor | 1.1463 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | -0.1158 |
| sortino_ratio | -0.0358 |
| max_drawdown | 0.2579 |
| cagr | -0.0245 |
| net_avg_win | 94.9229 |
| net_avg_loss | -112.7581 |
| avg_hold_time_bars | 28.0244 |
| exposure | 0.5831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
