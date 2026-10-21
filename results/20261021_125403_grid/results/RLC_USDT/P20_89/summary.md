# EMA Hourly Continuation — RLC/USDT P20_89

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.8050 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0347 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.5684 |
| sortino_ratio | -0.5244 |
| max_drawdown | 0.5089 |
| cagr | -0.2154 |
| net_avg_win | 67.7494 |
| net_avg_loss | -88.2895 |
| avg_hold_time_bars | 14.2799 |
| exposure | 0.3525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
