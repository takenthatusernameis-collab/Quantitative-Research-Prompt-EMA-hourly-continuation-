# EMA Hourly Continuation — INJ/USDT P8_26

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.7768 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 0.9979 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.8297 |
| sortino_ratio | -0.6518 |
| max_drawdown | 0.5681 |
| cagr | -0.2594 |
| net_avg_win | 59.2561 |
| net_avg_loss | -77.7872 |
| avg_hold_time_bars | 6.8328 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
