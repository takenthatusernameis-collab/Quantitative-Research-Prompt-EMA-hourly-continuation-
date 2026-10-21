# EMA Hourly Continuation — FET/USDT P21_89

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.8036 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.3453 |
| sortino_ratio | -0.4000 |
| max_drawdown | 0.4104 |
| cagr | -0.1694 |
| net_avg_win | 71.5359 |
| net_avg_loss | -86.1908 |
| avg_hold_time_bars | 18.9515 |
| exposure | 0.3730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
