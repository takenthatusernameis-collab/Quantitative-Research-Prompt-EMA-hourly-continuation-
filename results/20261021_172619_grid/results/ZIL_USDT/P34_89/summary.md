# EMA Hourly Continuation — ZIL/USDT P34_89

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.3579 |
| sortino_ratio | -0.7145 |
| max_drawdown | 0.6159 |
| cagr | -0.2797 |
| net_avg_win | 63.1695 |
| net_avg_loss | -84.9189 |
| avg_hold_time_bars | 9.9576 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
