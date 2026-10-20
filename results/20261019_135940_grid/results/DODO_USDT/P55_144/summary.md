# EMA Hourly Continuation — DODO/USDT P55_144

**Symbol:** DODO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8289 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -4.5090 |
| sortino_ratio | -1.5294 |
| max_drawdown | 0.8415 |
| cagr | -0.5128 |
| net_avg_win | 39.6865 |
| net_avg_loss | -58.4595 |
| avg_hold_time_bars | 9.6003 |
| exposure | 0.2511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
