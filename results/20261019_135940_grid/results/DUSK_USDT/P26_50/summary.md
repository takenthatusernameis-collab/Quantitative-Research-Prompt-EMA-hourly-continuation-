# EMA Hourly Continuation — DUSK/USDT P26_50

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.5224 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -6.9192 |
| sortino_ratio | -2.9554 |
| max_drawdown | 0.9739 |
| cagr | -0.7632 |
| net_avg_win | 26.2175 |
| net_avg_loss | -39.4114 |
| avg_hold_time_bars | 3.8169 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
