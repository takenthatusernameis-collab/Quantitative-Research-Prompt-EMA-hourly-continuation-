# EMA Hourly Continuation — MERL/USDT P26_89

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7783 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -1.7222 |
| sortino_ratio | -0.5266 |
| max_drawdown | 0.4908 |
| cagr | -0.2159 |
| net_avg_win | 72.4529 |
| net_avg_loss | -86.4473 |
| avg_hold_time_bars | 14.5294 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
