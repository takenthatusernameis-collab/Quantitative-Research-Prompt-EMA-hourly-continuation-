# EMA Hourly Continuation — 1INCH/USDT P20_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1338 |
| net_profit_factor | 0.0965 |
| net_win_rate | 0.2728 |
| gross_profit_factor | 0.5298 |
| gross_win_rate | 0.3834 |
| sharpe_ratio | -19.8116 |
| sortino_ratio | -11.2593 |
| max_drawdown | 1.0000 |
| cagr | -0.9982 |
| net_avg_win | 2.9265 |
| net_avg_loss | -11.3753 |
| avg_hold_time_bars | 1.6599 |
| exposure | 0.1010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
