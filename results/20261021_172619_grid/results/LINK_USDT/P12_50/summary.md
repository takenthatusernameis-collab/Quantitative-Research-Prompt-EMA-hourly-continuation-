# EMA Hourly Continuation — LINK/USDT P12_50

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7616 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 1.0016 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.5145 |
| sortino_ratio | -0.8772 |
| max_drawdown | 0.6748 |
| cagr | -0.3319 |
| net_avg_win | 69.9180 |
| net_avg_loss | -87.8767 |
| avg_hold_time_bars | 10.5345 |
| exposure | 0.2849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
