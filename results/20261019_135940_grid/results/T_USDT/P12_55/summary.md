# EMA Hourly Continuation — T/USDT P12_55

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 811 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -5.1211 |
| sortino_ratio | -2.0488 |
| max_drawdown | 0.9174 |
| cagr | -0.6262 |
| net_avg_win | 33.6820 |
| net_avg_loss | -51.1569 |
| avg_hold_time_bars | 10.4427 |
| exposure | 0.3832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
