# EMA Hourly Continuation — BIGTIME/USDT P12_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -2.7166 |
| sortino_ratio | -0.9940 |
| max_drawdown | 0.6918 |
| cagr | -0.3661 |
| net_avg_win | 51.9748 |
| net_avg_loss | -71.3044 |
| avg_hold_time_bars | 6.9390 |
| exposure | 0.2060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
