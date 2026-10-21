# EMA Hourly Continuation — SEI/USDT P26_50

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6592 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -2.5510 |
| sortino_ratio | -0.7095 |
| max_drawdown | 0.5723 |
| cagr | -0.2776 |
| net_avg_win | 60.6364 |
| net_avg_loss | -81.0607 |
| avg_hold_time_bars | 6.4447 |
| exposure | 0.1113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
