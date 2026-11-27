# EMA Hourly Continuation — SHR/USDT P100_144

**Symbol:** SHR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.3713 |
| net_win_rate | 0.3047 |
| gross_profit_factor | 0.5637 |
| gross_win_rate | 0.3047 |
| sharpe_ratio | -9.3717 |
| sortino_ratio | -3.4195 |
| max_drawdown | 0.9864 |
| cagr | -0.8168 |
| net_avg_win | 28.2759 |
| net_avg_loss | -33.3756 |
| avg_hold_time_bars | 4.1583 |
| exposure | 0.1272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
