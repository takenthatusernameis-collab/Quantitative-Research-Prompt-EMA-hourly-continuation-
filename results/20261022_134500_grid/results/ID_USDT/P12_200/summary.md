# EMA Hourly Continuation — ID/USDT P12_200

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7575 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0615 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -1.5953 |
| sortino_ratio | -0.4347 |
| max_drawdown | 0.4314 |
| cagr | -0.1862 |
| net_avg_win | 67.7148 |
| net_avg_loss | -89.8682 |
| avg_hold_time_bars | 43.3298 |
| exposure | 0.7314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
