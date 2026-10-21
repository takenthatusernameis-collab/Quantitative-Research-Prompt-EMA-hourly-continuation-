# EMA Hourly Continuation — NYM/USDT P26_34

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.2878 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.5968 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -5.2373 |
| sortino_ratio | -1.2100 |
| max_drawdown | 0.7599 |
| cagr | -0.4334 |
| net_avg_win | 31.9845 |
| net_avg_loss | -67.5283 |
| avg_hold_time_bars | 8.6732 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
