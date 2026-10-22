# EMA Hourly Continuation — STRAX/USDT P21_34

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.5082 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.7882 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -4.7286 |
| sortino_ratio | -1.5362 |
| max_drawdown | 0.8313 |
| cagr | -0.5081 |
| net_avg_win | 37.4548 |
| net_avg_loss | -59.0072 |
| avg_hold_time_bars | 6.8350 |
| exposure | 0.1609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
