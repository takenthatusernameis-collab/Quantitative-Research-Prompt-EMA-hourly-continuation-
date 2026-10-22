# EMA Hourly Continuation — LQTY/USDT P12_50

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7671 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -2.0501 |
| sortino_ratio | -0.7468 |
| max_drawdown | 0.5941 |
| cagr | -0.2908 |
| net_avg_win | 58.7463 |
| net_avg_loss | -76.8196 |
| avg_hold_time_bars | 12.9923 |
| exposure | 0.3816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
