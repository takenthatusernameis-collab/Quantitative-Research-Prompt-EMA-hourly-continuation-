# EMA Hourly Continuation — TURBO/USDT P100_144

**Symbol:** TURBO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -4.2394 |
| sortino_ratio | -1.3602 |
| max_drawdown | 0.7583 |
| cagr | -0.4789 |
| net_avg_win | 50.9739 |
| net_avg_loss | -76.3563 |
| avg_hold_time_bars | 3.8545 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
