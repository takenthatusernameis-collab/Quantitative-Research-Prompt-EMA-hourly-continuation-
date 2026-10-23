# EMA Hourly Continuation — AGLD/USDT P26_144

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.7101 |
| sortino_ratio | -0.8825 |
| max_drawdown | 0.6876 |
| cagr | -0.3388 |
| net_avg_win | 62.6841 |
| net_avg_loss | -82.8963 |
| avg_hold_time_bars | 19.7148 |
| exposure | 0.4755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
