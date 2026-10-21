# EMA Hourly Continuation — FLOKI/USDT P21_50

**Symbol:** FLOKI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7239 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -2.4702 |
| sortino_ratio | -0.7837 |
| max_drawdown | 0.6311 |
| cagr | -0.3025 |
| net_avg_win | 66.1384 |
| net_avg_loss | -83.5742 |
| avg_hold_time_bars | 7.3239 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
