# EMA Hourly Continuation — ZEN/USDT P12_50

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.5278 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.8787 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -7.1020 |
| sortino_ratio | -3.3010 |
| max_drawdown | 0.9831 |
| cagr | -0.7989 |
| net_avg_win | 22.6346 |
| net_avg_loss | -34.2663 |
| avg_hold_time_bars | 7.2830 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
