# EMA Hourly Continuation — SEI/USDT P12_50

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9924 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.9485 |
| sortino_ratio | -0.6861 |
| max_drawdown | 0.5569 |
| cagr | -0.2715 |
| net_avg_win | 70.7291 |
| net_avg_loss | -87.0412 |
| avg_hold_time_bars | 11.8264 |
| exposure | 0.3252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
