# EMA Hourly Continuation — 1INCH/USDT P21_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5079 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.8428 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -5.5987 |
| sortino_ratio | -1.9694 |
| max_drawdown | 0.9138 |
| cagr | -0.6189 |
| net_avg_win | 34.4505 |
| net_avg_loss | -52.0172 |
| avg_hold_time_bars | 16.6582 |
| exposure | 0.4763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
