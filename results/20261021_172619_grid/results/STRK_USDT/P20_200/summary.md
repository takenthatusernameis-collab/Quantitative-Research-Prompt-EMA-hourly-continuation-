# EMA Hourly Continuation — STRK/USDT P20_200

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -0.7056 |
| sortino_ratio | -0.1715 |
| max_drawdown | 0.2490 |
| cagr | -0.0784 |
| net_avg_win | 84.8842 |
| net_avg_loss | -99.0384 |
| avg_hold_time_bars | 48.0799 |
| exposure | 0.6294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
