# EMA Hourly Continuation — DOGE/USDT P20_100

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6931 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.4075 |
| sortino_ratio | -0.6869 |
| max_drawdown | 0.5919 |
| cagr | -0.2710 |
| net_avg_win | 65.4576 |
| net_avg_loss | -84.2013 |
| avg_hold_time_bars | 24.4289 |
| exposure | 0.4453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
