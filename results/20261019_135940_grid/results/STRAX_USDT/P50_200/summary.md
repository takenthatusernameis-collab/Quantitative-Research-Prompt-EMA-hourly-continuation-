# EMA Hourly Continuation — STRAX/USDT P50_200

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5256 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -4.7053 |
| sortino_ratio | -1.4546 |
| max_drawdown | 0.8215 |
| cagr | -0.4951 |
| net_avg_win | 45.1113 |
| net_avg_loss | -62.7342 |
| avg_hold_time_bars | 17.1050 |
| exposure | 0.3723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
