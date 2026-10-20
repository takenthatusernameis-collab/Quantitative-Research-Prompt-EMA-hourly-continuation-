# EMA Hourly Continuation — SATS/USDT P89_200

**Symbol:** SATS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5515 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -3.4449 |
| sortino_ratio | -0.9336 |
| max_drawdown | 0.6774 |
| cagr | -0.3545 |
| net_avg_win | 50.1340 |
| net_avg_loss | -72.0154 |
| avg_hold_time_bars | 12.6146 |
| exposure | 0.2118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
