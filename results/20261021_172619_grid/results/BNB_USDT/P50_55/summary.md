# EMA Hourly Continuation — BNB/USDT P50_55

**Symbol:** BNB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.6822 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3106 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.9337 |
| sortino_ratio | -0.1204 |
| max_drawdown | 0.1738 |
| cagr | -0.0511 |
| net_avg_win | 60.2014 |
| net_avg_loss | -117.6553 |
| avg_hold_time_bars | 4.2338 |
| exposure | 0.0148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
