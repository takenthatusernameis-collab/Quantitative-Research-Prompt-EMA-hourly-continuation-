# EMA Hourly Continuation — ARKM/USDT P34_89

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7589 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.8166 |
| sortino_ratio | -0.5253 |
| max_drawdown | 0.4933 |
| cagr | -0.2150 |
| net_avg_win | 72.0539 |
| net_avg_loss | -89.5483 |
| avg_hold_time_bars | 10.4146 |
| exposure | 0.1941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
