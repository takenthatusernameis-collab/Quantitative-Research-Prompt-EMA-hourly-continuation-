# EMA Hourly Continuation — ANKR/USDT P100_200

**Symbol:** ANKR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5715 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9378 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.5837 |
| sortino_ratio | -1.0205 |
| max_drawdown | 0.7057 |
| cagr | -0.3813 |
| net_avg_win | 49.9721 |
| net_avg_loss | -76.7630 |
| avg_hold_time_bars | 11.9225 |
| exposure | 0.2168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
