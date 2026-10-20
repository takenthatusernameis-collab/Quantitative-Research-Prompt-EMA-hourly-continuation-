# EMA Hourly Continuation — MINA/USDT P12_200

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0516 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -1.3673 |
| sortino_ratio | -0.3658 |
| max_drawdown | 0.4428 |
| cagr | -0.1609 |
| net_avg_win | 64.8931 |
| net_avg_loss | -89.6127 |
| avg_hold_time_bars | 46.0840 |
| exposure | 0.7478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
