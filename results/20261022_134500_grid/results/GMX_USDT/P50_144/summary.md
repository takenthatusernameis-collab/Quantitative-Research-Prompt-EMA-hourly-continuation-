# EMA Hourly Continuation — GMX/USDT P50_144

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.5521 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -4.4056 |
| sortino_ratio | -1.4405 |
| max_drawdown | 0.8283 |
| cagr | -0.4991 |
| net_avg_win | 42.4870 |
| net_avg_loss | -60.7014 |
| avg_hold_time_bars | 10.9742 |
| exposure | 0.2704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
