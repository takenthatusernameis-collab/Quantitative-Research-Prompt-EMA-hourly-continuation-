# EMA Hourly Continuation — AR/USDT P20_55

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.4716 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.7377 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -6.6822 |
| sortino_ratio | -2.9165 |
| max_drawdown | 0.9710 |
| cagr | -0.7559 |
| net_avg_win | 20.4848 |
| net_avg_loss | -34.0913 |
| avg_hold_time_bars | 5.4023 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
