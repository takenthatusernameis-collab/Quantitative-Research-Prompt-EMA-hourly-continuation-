# EMA Hourly Continuation — ORCA/USDT P50_200

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -1.7799 |
| sortino_ratio | -0.4389 |
| max_drawdown | 0.4531 |
| cagr | -0.1841 |
| net_avg_win | 64.4474 |
| net_avg_loss | -84.0543 |
| avg_hold_time_bars | 27.3675 |
| exposure | 0.3757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
