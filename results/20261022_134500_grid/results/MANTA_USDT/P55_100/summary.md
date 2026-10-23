# EMA Hourly Continuation — MANTA/USDT P55_100

**Symbol:** MANTA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.5249 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -5.2356 |
| sortino_ratio | -1.8512 |
| max_drawdown | 0.8935 |
| cagr | -0.5879 |
| net_avg_win | 35.2044 |
| net_avg_loss | -54.4288 |
| avg_hold_time_bars | 5.7712 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
