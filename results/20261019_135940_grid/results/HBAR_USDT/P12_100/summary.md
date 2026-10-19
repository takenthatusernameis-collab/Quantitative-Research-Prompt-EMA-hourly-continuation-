# EMA Hourly Continuation — HBAR/USDT P12_100

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.6128 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9545 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -4.2794 |
| sortino_ratio | -1.6175 |
| max_drawdown | 0.8743 |
| cagr | -0.5424 |
| net_avg_win | 39.0897 |
| net_avg_loss | -59.1988 |
| avg_hold_time_bars | 16.4053 |
| exposure | 0.5391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
