# EMA Hourly Continuation — WEMIX/USDT P20_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.2768 |
| net_win_rate | 0.2947 |
| gross_profit_factor | 0.4858 |
| gross_win_rate | 0.3062 |
| sharpe_ratio | -14.1274 |
| sortino_ratio | -6.8105 |
| max_drawdown | 0.9998 |
| cagr | -0.9675 |
| net_avg_win | 11.4944 |
| net_avg_loss | -17.3473 |
| avg_hold_time_bars | 8.4920 |
| exposure | 0.4362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
