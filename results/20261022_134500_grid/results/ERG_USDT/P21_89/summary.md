# EMA Hourly Continuation — ERG/USDT P21_89

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.4291 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.6849 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -6.5521 |
| sortino_ratio | -2.5349 |
| max_drawdown | 0.9561 |
| cagr | -0.7092 |
| net_avg_win | 22.7857 |
| net_avg_loss | -38.1039 |
| avg_hold_time_bars | 10.2361 |
| exposure | 0.3508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
