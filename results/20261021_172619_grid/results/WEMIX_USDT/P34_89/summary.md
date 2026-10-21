# EMA Hourly Continuation — WEMIX/USDT P34_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.4655 |
| net_win_rate | 0.3678 |
| gross_profit_factor | 0.6003 |
| gross_win_rate | 0.3678 |
| sharpe_ratio | -4.9657 |
| sortino_ratio | -1.3967 |
| max_drawdown | 0.8047 |
| cagr | -0.4781 |
| net_avg_win | 48.0113 |
| net_avg_loss | -59.9869 |
| avg_hold_time_bars | 12.6902 |
| exposure | 0.2290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
