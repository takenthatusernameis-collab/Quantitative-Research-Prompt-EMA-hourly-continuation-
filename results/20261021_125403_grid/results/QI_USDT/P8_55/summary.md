# EMA Hourly Continuation — QI/USDT P8_55

**Symbol:** QI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -3.1167 |
| sortino_ratio | -1.1804 |
| max_drawdown | 0.7704 |
| cagr | -0.4194 |
| net_avg_win | 59.3579 |
| net_avg_loss | -73.2812 |
| avg_hold_time_bars | 14.3056 |
| exposure | 0.4596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
