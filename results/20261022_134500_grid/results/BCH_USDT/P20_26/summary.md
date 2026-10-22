# EMA Hourly Continuation — BCH/USDT P20_26

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1190 |
| net_profit_factor | 0.1525 |
| net_win_rate | 0.3084 |
| gross_profit_factor | 0.6407 |
| gross_win_rate | 0.3849 |
| sharpe_ratio | -17.0408 |
| sortino_ratio | -8.8512 |
| max_drawdown | 1.0000 |
| cagr | -0.9924 |
| net_avg_win | 4.9021 |
| net_avg_loss | -14.3366 |
| avg_hold_time_bars | 1.9899 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
