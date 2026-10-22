# EMA Hourly Continuation — MANTA/USDT P34_144

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7471 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -1.7102 |
| sortino_ratio | -0.4526 |
| max_drawdown | 0.4079 |
| cagr | -0.1883 |
| net_avg_win | 73.9097 |
| net_avg_loss | -88.1126 |
| avg_hold_time_bars | 27.8295 |
| exposure | 0.4377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
