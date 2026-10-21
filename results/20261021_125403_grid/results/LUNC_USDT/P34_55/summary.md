# EMA Hourly Continuation — LUNC/USDT P34_55

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.6214 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.3712 |
| sortino_ratio | -0.5662 |
| max_drawdown | 0.5073 |
| cagr | -0.2276 |
| net_avg_win | 59.3349 |
| net_avg_loss | -86.3318 |
| avg_hold_time_bars | 5.8741 |
| exposure | 0.0742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
