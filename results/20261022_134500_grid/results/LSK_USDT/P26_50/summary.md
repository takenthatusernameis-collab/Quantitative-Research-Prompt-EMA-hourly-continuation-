# EMA Hourly Continuation — LSK/USDT P26_50

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -6.2964 |
| sortino_ratio | -2.5327 |
| max_drawdown | 0.9563 |
| cagr | -0.7083 |
| net_avg_win | 23.2167 |
| net_avg_loss | -43.1748 |
| avg_hold_time_bars | 4.7038 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
