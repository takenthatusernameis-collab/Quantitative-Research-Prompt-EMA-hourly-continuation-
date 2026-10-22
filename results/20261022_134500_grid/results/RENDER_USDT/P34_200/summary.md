# EMA Hourly Continuation — RENDER/USDT P34_200

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7637 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0011 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.4881 |
| sortino_ratio | -0.3942 |
| max_drawdown | 0.3805 |
| cagr | -0.1688 |
| net_avg_win | 70.5235 |
| net_avg_loss | -94.2199 |
| avg_hold_time_bars | 33.1505 |
| exposure | 0.5231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
