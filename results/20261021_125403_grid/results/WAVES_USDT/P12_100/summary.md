# EMA Hourly Continuation — WAVES/USDT P12_100

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7716 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9964 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -2.0867 |
| sortino_ratio | -0.7086 |
| max_drawdown | 0.5969 |
| cagr | -0.2798 |
| net_avg_win | 67.7385 |
| net_avg_loss | -86.5551 |
| avg_hold_time_bars | 20.2801 |
| exposure | 0.5199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
