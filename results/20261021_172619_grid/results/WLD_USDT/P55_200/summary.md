# EMA Hourly Continuation — WLD/USDT P55_200

**Symbol:** WLD/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.8860 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0086 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -0.5222 |
| sortino_ratio | -0.1172 |
| max_drawdown | 0.2138 |
| cagr | -0.0550 |
| net_avg_win | 82.9752 |
| net_avg_loss | -95.9722 |
| avg_hold_time_bars | 32.7837 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
