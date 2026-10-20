# EMA Hourly Continuation — BLUR/USDT P144_200

**Symbol:** BLUR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.4810 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8643 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.0312 |
| sortino_ratio | -1.1144 |
| max_drawdown | 0.7453 |
| cagr | -0.4137 |
| net_avg_win | 38.3143 |
| net_avg_loss | -70.9366 |
| avg_hold_time_bars | 4.4605 |
| exposure | 0.0767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
