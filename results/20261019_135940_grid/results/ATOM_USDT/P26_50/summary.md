# EMA Hourly Continuation — ATOM/USDT P26_50

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.3622 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.7874 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -8.2808 |
| sortino_ratio | -3.5273 |
| max_drawdown | 0.9879 |
| cagr | -0.8246 |
| net_avg_win | 14.1953 |
| net_avg_loss | -30.8998 |
| avg_hold_time_bars | 3.6875 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
