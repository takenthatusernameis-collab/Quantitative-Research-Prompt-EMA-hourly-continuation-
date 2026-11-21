# EMA Hourly Continuation — HTR/USDT P55_200

**Symbol:** HTR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5266 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7667 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -5.1563 |
| sortino_ratio | -1.6137 |
| max_drawdown | 0.8784 |
| cagr | -0.5578 |
| net_avg_win | 45.2933 |
| net_avg_loss | -61.9688 |
| avg_hold_time_bars | 14.3072 |
| exposure | 0.3323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
