# EMA Hourly Continuation — GMX/USDT P20_50

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.4762 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -8.1078 |
| sortino_ratio | -3.6067 |
| max_drawdown | 0.9879 |
| cagr | -0.8260 |
| net_avg_win | 21.6368 |
| net_avg_loss | -32.9067 |
| avg_hold_time_bars | 5.2834 |
| exposure | 0.2373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
