# EMA Hourly Continuation — MTL/USDT P8_26

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1398 |
| net_profit_factor | 0.4586 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.9234 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -10.5521 |
| sortino_ratio | -5.5578 |
| max_drawdown | 0.9991 |
| cagr | -0.9370 |
| net_avg_win | 14.1727 |
| net_avg_loss | -23.0359 |
| avg_hold_time_bars | 5.2139 |
| exposure | 0.3298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
