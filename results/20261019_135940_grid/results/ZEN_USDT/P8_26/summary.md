# EMA Hourly Continuation — ZEN/USDT P8_26

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1635 |
| net_profit_factor | 0.3685 |
| net_win_rate | 0.4349 |
| gross_profit_factor | 0.7527 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -10.4677 |
| sortino_ratio | -5.9571 |
| max_drawdown | 0.9994 |
| cagr | -0.9476 |
| net_avg_win | 8.2012 |
| net_avg_loss | -17.1266 |
| avg_hold_time_bars | 3.6716 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
