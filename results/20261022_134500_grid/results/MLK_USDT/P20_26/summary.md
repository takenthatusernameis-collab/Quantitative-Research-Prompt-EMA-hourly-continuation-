# EMA Hourly Continuation — MLK/USDT P20_26

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.1064 |
| net_win_rate | 0.1923 |
| gross_profit_factor | 0.4442 |
| gross_win_rate | 0.2288 |
| sharpe_ratio | -22.9899 |
| sortino_ratio | -13.6049 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 4.1061 |
| net_avg_loss | -9.1878 |
| avg_hold_time_bars | 2.1399 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
