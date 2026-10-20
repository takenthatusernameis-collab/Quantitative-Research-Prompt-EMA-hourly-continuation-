# EMA Hourly Continuation — EDU/USDT P34_89

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8239 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -4.8449 |
| sortino_ratio | -1.8482 |
| max_drawdown | 0.8972 |
| cagr | -0.5845 |
| net_avg_win | 32.1804 |
| net_avg_loss | -49.2665 |
| avg_hold_time_bars | 7.4720 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
