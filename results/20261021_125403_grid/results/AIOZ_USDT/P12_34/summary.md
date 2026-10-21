# EMA Hourly Continuation — AIOZ/USDT P12_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.7097 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.0777 |
| sortino_ratio | -1.0671 |
| max_drawdown | 0.7329 |
| cagr | -0.3876 |
| net_avg_win | 63.1971 |
| net_avg_loss | -76.2422 |
| avg_hold_time_bars | 6.4714 |
| exposure | 0.1747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
