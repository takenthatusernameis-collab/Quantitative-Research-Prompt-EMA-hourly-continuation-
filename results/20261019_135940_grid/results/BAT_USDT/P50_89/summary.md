# EMA Hourly Continuation — BAT/USDT P50_89

**Symbol:** BAT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.4367 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8508 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -6.0850 |
| sortino_ratio | -2.2013 |
| max_drawdown | 0.9314 |
| cagr | -0.6532 |
| net_avg_win | 25.2104 |
| net_avg_loss | -45.3575 |
| avg_hold_time_bars | 4.7169 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
