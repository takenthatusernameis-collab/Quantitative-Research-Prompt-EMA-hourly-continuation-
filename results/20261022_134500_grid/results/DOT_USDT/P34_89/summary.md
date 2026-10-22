# EMA Hourly Continuation — DOT/USDT P34_89

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9648 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.5979 |
| sortino_ratio | -1.6795 |
| max_drawdown | 0.8743 |
| cagr | -0.5582 |
| net_avg_win | 36.2289 |
| net_avg_loss | -58.9799 |
| avg_hold_time_bars | 7.3294 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
