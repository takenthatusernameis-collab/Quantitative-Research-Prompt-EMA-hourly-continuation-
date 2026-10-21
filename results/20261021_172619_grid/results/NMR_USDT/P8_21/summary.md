# EMA Hourly Continuation — NMR/USDT P8_21

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -4.0648 |
| sortino_ratio | -1.5193 |
| max_drawdown | 0.8411 |
| cagr | -0.5028 |
| net_avg_win | 44.7272 |
| net_avg_loss | -62.8045 |
| avg_hold_time_bars | 5.1669 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
