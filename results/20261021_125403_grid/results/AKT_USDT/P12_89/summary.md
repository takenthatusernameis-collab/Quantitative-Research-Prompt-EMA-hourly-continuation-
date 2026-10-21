# EMA Hourly Continuation — AKT/USDT P12_89

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8297 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.2993 |
| sortino_ratio | -0.4126 |
| max_drawdown | 0.4117 |
| cagr | -0.1754 |
| net_avg_win | 76.3432 |
| net_avg_loss | -90.8995 |
| avg_hold_time_bars | 21.7688 |
| exposure | 0.4878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
