# EMA Hourly Continuation — SUN/USDT P8_20

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1452 |
| net_profit_factor | 0.1338 |
| net_win_rate | 0.3574 |
| gross_profit_factor | 0.6038 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -16.3468 |
| sortino_ratio | -9.0968 |
| max_drawdown | 1.0000 |
| cagr | -0.9925 |
| net_avg_win | 2.9768 |
| net_avg_loss | -12.3740 |
| avg_hold_time_bars | 4.1605 |
| exposure | 0.2734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
