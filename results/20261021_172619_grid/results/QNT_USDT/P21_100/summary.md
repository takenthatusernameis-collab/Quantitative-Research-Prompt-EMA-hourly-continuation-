# EMA Hourly Continuation — QNT/USDT P21_100

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7950 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0558 |
| gross_win_rate | 0.5167 |
| sharpe_ratio | -1.5926 |
| sortino_ratio | -0.5315 |
| max_drawdown | 0.4919 |
| cagr | -0.2170 |
| net_avg_win | 64.0182 |
| net_avg_loss | -86.1029 |
| avg_hold_time_bars | 14.6320 |
| exposure | 0.3578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
