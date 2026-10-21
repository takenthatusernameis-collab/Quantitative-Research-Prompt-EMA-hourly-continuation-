# EMA Hourly Continuation — BOME/USDT P12_21

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9630 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.6707 |
| sortino_ratio | -0.4096 |
| max_drawdown | 0.4245 |
| cagr | -0.1716 |
| net_avg_win | 72.2684 |
| net_avg_loss | -95.1282 |
| avg_hold_time_bars | 4.3788 |
| exposure | 0.0583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
