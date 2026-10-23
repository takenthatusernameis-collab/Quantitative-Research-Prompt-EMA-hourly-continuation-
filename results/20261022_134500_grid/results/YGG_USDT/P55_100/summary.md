# EMA Hourly Continuation — YGG/USDT P55_100

**Symbol:** YGG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6205 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.8995 |
| sortino_ratio | -1.4043 |
| max_drawdown | 0.8217 |
| cagr | -0.4813 |
| net_avg_win | 42.2660 |
| net_avg_loss | -64.4107 |
| avg_hold_time_bars | 5.1553 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
