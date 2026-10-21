# EMA Hourly Continuation — KMNO/USDT P12_34

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.8130 |
| net_win_rate | 0.5233 |
| gross_profit_factor | 1.0823 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -1.4793 |
| sortino_ratio | -0.5163 |
| max_drawdown | 0.4722 |
| cagr | -0.2130 |
| net_avg_win | 64.1267 |
| net_avg_loss | -86.5924 |
| avg_hold_time_bars | 7.4663 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
