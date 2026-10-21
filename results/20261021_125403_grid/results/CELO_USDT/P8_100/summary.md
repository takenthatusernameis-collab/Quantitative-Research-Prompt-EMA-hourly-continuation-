# EMA Hourly Continuation — CELO/USDT P8_100

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8904 |
| net_win_rate | 0.5185 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -0.8748 |
| sortino_ratio | -0.2764 |
| max_drawdown | 0.4212 |
| cagr | -0.1232 |
| net_avg_win | 90.9953 |
| net_avg_loss | -110.0576 |
| avg_hold_time_bars | 30.5967 |
| exposure | 0.6729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
