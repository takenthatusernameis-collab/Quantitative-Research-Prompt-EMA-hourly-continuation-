# EMA Hourly Continuation — METIS/USDT P21_200

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7321 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -1.7123 |
| sortino_ratio | -0.4150 |
| max_drawdown | 0.4082 |
| cagr | -0.1746 |
| net_avg_win | 77.3738 |
| net_avg_loss | -90.8818 |
| avg_hold_time_bars | 46.4795 |
| exposure | 0.6169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
