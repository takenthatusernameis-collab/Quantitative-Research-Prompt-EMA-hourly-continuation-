# EMA Hourly Continuation — VET/USDT P26_89

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7937 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0406 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.5284 |
| sortino_ratio | -0.4807 |
| max_drawdown | 0.4646 |
| cagr | -0.1989 |
| net_avg_win | 66.7839 |
| net_avg_loss | -88.8376 |
| avg_hold_time_bars | 12.8956 |
| exposure | 0.2808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
