# EMA Hourly Continuation — AGLD/USDT P100_200

**Symbol:** AGLD/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6808 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.4904 |
| sortino_ratio | -0.7071 |
| max_drawdown | 0.5812 |
| cagr | -0.2787 |
| net_avg_win | 61.4088 |
| net_avg_loss | -85.7970 |
| avg_hold_time_bars | 10.4775 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
