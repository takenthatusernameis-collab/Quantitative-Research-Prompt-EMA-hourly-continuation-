# EMA Hourly Continuation — STRK/USDT P21_200

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8660 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -0.7171 |
| sortino_ratio | -0.1743 |
| max_drawdown | 0.2726 |
| cagr | -0.0796 |
| net_avg_win | 83.7818 |
| net_avg_loss | -98.1021 |
| avg_hold_time_bars | 47.5312 |
| exposure | 0.6222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
