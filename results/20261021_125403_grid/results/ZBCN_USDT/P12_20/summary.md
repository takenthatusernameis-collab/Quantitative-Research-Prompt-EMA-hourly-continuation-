# EMA Hourly Continuation — ZBCN/USDT P12_20

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.8847 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1153 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.5219 |
| sortino_ratio | -0.1153 |
| max_drawdown | 0.1737 |
| cagr | -0.0537 |
| net_avg_win | 80.0744 |
| net_avg_loss | -102.2378 |
| avg_hold_time_bars | 5.4913 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
