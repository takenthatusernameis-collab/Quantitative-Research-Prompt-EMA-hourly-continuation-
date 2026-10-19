# EMA Hourly Continuation — CRV/USDT P26_89

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6175 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -4.2477 |
| sortino_ratio | -1.6261 |
| max_drawdown | 0.8651 |
| cagr | -0.5390 |
| net_avg_win | 39.4186 |
| net_avg_loss | -58.4992 |
| avg_hold_time_bars | 8.6104 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
