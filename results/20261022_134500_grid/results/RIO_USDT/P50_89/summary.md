# EMA Hourly Continuation — RIO/USDT P50_89

**Symbol:** RIO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.4437 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.6560 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -7.7036 |
| sortino_ratio | -3.0213 |
| max_drawdown | 0.9759 |
| cagr | -0.7741 |
| net_avg_win | 26.0159 |
| net_avg_loss | -36.9078 |
| avg_hold_time_bars | 3.7920 |
| exposure | 0.1347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
