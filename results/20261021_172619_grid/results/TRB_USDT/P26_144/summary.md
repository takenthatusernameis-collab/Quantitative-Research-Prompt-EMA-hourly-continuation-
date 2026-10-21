# EMA Hourly Continuation — TRB/USDT P26_144

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.0245 |
| sortino_ratio | -0.5614 |
| max_drawdown | 0.4999 |
| cagr | -0.2279 |
| net_avg_win | 68.8027 |
| net_avg_loss | -85.4607 |
| avg_hold_time_bars | 27.6194 |
| exposure | 0.4762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
