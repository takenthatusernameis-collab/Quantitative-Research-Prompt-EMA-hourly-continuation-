# EMA Hourly Continuation — SLP/USDT P26_55

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.5269 |
| net_win_rate | 0.4269 |
| gross_profit_factor | 0.9183 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -8.6388 |
| sortino_ratio | -3.9612 |
| max_drawdown | 0.9930 |
| cagr | -0.8586 |
| net_avg_win | 24.7315 |
| net_avg_loss | -34.9691 |
| avg_hold_time_bars | 3.9016 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
