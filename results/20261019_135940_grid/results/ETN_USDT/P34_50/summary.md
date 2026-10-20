# EMA Hourly Continuation — ETN/USDT P34_50

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.2367 |
| net_win_rate | 0.3201 |
| gross_profit_factor | 0.4357 |
| gross_win_rate | 0.3492 |
| sharpe_ratio | -13.2662 |
| sortino_ratio | -6.1012 |
| max_drawdown | 0.9987 |
| cagr | -0.9571 |
| net_avg_win | 11.2612 |
| net_avg_loss | -22.4032 |
| avg_hold_time_bars | 2.8428 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
