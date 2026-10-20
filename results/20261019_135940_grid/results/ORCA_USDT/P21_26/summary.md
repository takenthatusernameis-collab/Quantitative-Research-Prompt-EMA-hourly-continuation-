# EMA Hourly Continuation — ORCA/USDT P21_26

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.3207 |
| net_win_rate | 0.3923 |
| gross_profit_factor | 0.8377 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -11.8688 |
| sortino_ratio | -5.5341 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 11.2615 |
| net_avg_loss | -22.6696 |
| avg_hold_time_bars | 2.6330 |
| exposure | 0.1278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
