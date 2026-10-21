# EMA Hourly Continuation — COMP/USDT P12_21

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.5101 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.7836 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -4.8821 |
| sortino_ratio | -1.5089 |
| max_drawdown | 0.8292 |
| cagr | -0.5022 |
| net_avg_win | 43.2488 |
| net_avg_loss | -63.6671 |
| avg_hold_time_bars | 4.5647 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
