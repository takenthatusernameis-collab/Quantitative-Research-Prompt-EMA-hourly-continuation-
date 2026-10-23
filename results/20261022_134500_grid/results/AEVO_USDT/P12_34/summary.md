# EMA Hourly Continuation — AEVO/USDT P12_34

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1265 |
| net_profit_factor | 0.4892 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8755 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -8.0312 |
| sortino_ratio | -4.0178 |
| max_drawdown | 0.9928 |
| cagr | -0.8579 |
| net_avg_win | 16.8886 |
| net_avg_loss | -27.6859 |
| avg_hold_time_bars | 4.4941 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
