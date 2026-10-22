# EMA Hourly Continuation — PUNDIX/USDT P21_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.8708 |
| sortino_ratio | -0.9652 |
| max_drawdown | 0.6816 |
| cagr | -0.3579 |
| net_avg_win | 54.5524 |
| net_avg_loss | -73.4373 |
| avg_hold_time_bars | 15.3712 |
| exposure | 0.3878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
