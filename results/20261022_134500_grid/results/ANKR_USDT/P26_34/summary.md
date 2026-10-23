# EMA Hourly Continuation — ANKR/USDT P26_34

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.2693 |
| net_win_rate | 0.3691 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -13.6120 |
| sortino_ratio | -6.5518 |
| max_drawdown | 0.9998 |
| cagr | -0.9681 |
| net_avg_win | 9.2356 |
| net_avg_loss | -20.0635 |
| avg_hold_time_bars | 3.4801 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
