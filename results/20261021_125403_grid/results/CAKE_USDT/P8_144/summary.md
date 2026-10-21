# EMA Hourly Continuation — CAKE/USDT P8_144

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7995 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.3911 |
| sortino_ratio | -0.3932 |
| max_drawdown | 0.4316 |
| cagr | -0.1667 |
| net_avg_win | 74.3606 |
| net_avg_loss | -94.4509 |
| avg_hold_time_bars | 40.3657 |
| exposure | 0.7174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
