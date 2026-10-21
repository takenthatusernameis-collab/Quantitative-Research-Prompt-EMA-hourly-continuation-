# EMA Hourly Continuation — ATOM/USDT P34_50

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.6405 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -1.9465 |
| sortino_ratio | -0.4058 |
| max_drawdown | 0.3774 |
| cagr | -0.1689 |
| net_avg_win | 64.2990 |
| net_avg_loss | -96.6324 |
| avg_hold_time_bars | 5.6762 |
| exposure | 0.0542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
