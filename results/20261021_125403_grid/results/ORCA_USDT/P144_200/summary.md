# EMA Hourly Continuation — ORCA/USDT P144_200

**Symbol:** ORCA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7040 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.9615 |
| sortino_ratio | -0.6203 |
| max_drawdown | 0.5259 |
| cagr | -0.2492 |
| net_avg_win | 53.7695 |
| net_avg_loss | -81.7138 |
| avg_hold_time_bars | 7.2995 |
| exposure | 0.0720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
