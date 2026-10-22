# EMA Hourly Continuation — XTZ/USDT P55_100

**Symbol:** XTZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -5.9515 |
| sortino_ratio | -2.2154 |
| max_drawdown | 0.9326 |
| cagr | -0.6548 |
| net_avg_win | 25.8107 |
| net_avg_loss | -47.1434 |
| avg_hold_time_bars | 5.3517 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
