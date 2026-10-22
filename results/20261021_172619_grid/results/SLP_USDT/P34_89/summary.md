# EMA Hourly Continuation — SLP/USDT P34_89

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7936 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.8086 |
| sortino_ratio | -0.5767 |
| max_drawdown | 0.5344 |
| cagr | -0.2337 |
| net_avg_win | 75.2935 |
| net_avg_loss | -96.4190 |
| avg_hold_time_bars | 9.8664 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
