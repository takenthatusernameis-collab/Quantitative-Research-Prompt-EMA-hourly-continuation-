# EMA Hourly Continuation — GRAM/USDT P21_200

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -4.2459 |
| sortino_ratio | -1.2627 |
| max_drawdown | 0.7956 |
| cagr | -0.4529 |
| net_avg_win | 42.8585 |
| net_avg_loss | -66.4796 |
| avg_hold_time_bars | 29.6772 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
