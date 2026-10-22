# EMA Hourly Continuation — LQTY/USDT P20_200

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7705 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9318 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -1.3016 |
| sortino_ratio | -0.3181 |
| max_drawdown | 0.3388 |
| cagr | -0.1367 |
| net_avg_win | 72.2240 |
| net_avg_loss | -89.3951 |
| avg_hold_time_bars | 50.5186 |
| exposure | 0.6744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
