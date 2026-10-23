# EMA Hourly Continuation — TRB/USDT P8_144

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8676 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.2394 |
| sortino_ratio | -0.9253 |
| max_drawdown | 0.6854 |
| cagr | -0.3581 |
| net_avg_win | 46.7565 |
| net_avg_loss | -70.8625 |
| avg_hold_time_bars | 41.4580 |
| exposure | 0.7823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
