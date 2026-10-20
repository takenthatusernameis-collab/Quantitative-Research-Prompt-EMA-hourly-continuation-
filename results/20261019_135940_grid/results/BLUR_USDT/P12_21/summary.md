# EMA Hourly Continuation — BLUR/USDT P12_21

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.3208 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.7329 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -12.1056 |
| sortino_ratio | -6.4777 |
| max_drawdown | 0.9997 |
| cagr | -0.9610 |
| net_avg_win | 8.2137 |
| net_avg_loss | -17.3586 |
| avg_hold_time_bars | 2.5123 |
| exposure | 0.1618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
