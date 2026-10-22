# EMA Hourly Continuation — JUP/USDT P21_200

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.5935 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8166 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -3.9727 |
| sortino_ratio | -1.1722 |
| max_drawdown | 0.7755 |
| cagr | -0.4338 |
| net_avg_win | 57.5271 |
| net_avg_loss | -73.6468 |
| avg_hold_time_bars | 28.9172 |
| exposure | 0.5875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
