# EMA Hourly Continuation — NYM/USDT P20_100

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.3134 |
| net_win_rate | 0.3534 |
| gross_profit_factor | 0.6232 |
| gross_win_rate | 0.3795 |
| sharpe_ratio | -8.7437 |
| sortino_ratio | -3.0445 |
| max_drawdown | 0.9831 |
| cagr | -0.7995 |
| net_avg_win | 20.6610 |
| net_avg_loss | -36.0371 |
| avg_hold_time_bars | 14.6743 |
| exposure | 0.4095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
