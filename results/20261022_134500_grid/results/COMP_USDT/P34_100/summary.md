# EMA Hourly Continuation — COMP/USDT P34_100

**Symbol:** COMP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -4.6314 |
| sortino_ratio | -1.6864 |
| max_drawdown | 0.8760 |
| cagr | -0.5609 |
| net_avg_win | 27.3583 |
| net_avg_loss | -49.8525 |
| avg_hold_time_bars | 9.8892 |
| exposure | 0.3043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
