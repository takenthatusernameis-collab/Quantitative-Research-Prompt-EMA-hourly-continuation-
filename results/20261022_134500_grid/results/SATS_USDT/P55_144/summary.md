# EMA Hourly Continuation — SATS/USDT P55_144

**Symbol:** SATS/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.4711 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.7114 |
| gross_win_rate | 0.4163 |
| sharpe_ratio | -4.5807 |
| sortino_ratio | -1.3511 |
| max_drawdown | 0.8060 |
| cagr | -0.4751 |
| net_avg_win | 39.7524 |
| net_avg_loss | -57.9689 |
| avg_hold_time_bars | 12.7602 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
