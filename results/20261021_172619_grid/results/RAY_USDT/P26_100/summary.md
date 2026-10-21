# EMA Hourly Continuation — RAY/USDT P26_100

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 1.0191 |
| net_win_rate | 0.5572 |
| gross_profit_factor | 1.2495 |
| gross_win_rate | 0.5572 |
| sharpe_ratio | 0.2011 |
| sortino_ratio | 0.0630 |
| max_drawdown | 0.2312 |
| cagr | 0.0182 |
| net_avg_win | 95.8367 |
| net_avg_loss | -118.3535 |
| avg_hold_time_bars | 13.6847 |
| exposure | 0.2880 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
