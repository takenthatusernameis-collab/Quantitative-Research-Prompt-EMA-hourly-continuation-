# EMA Hourly Continuation — ALGO/USDT P34_55

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0091 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.7303 |
| sortino_ratio | -0.4218 |
| max_drawdown | 0.4214 |
| cagr | -0.1749 |
| net_avg_win | 66.4065 |
| net_avg_loss | -94.7754 |
| avg_hold_time_bars | 5.3972 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
