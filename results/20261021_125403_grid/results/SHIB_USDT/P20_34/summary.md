# EMA Hourly Continuation — SHIB/USDT P20_34

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.8132 |
| net_win_rate | 0.5433 |
| gross_profit_factor | 1.1852 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | -1.0251 |
| sortino_ratio | -0.2368 |
| max_drawdown | 0.2828 |
| cagr | -0.1033 |
| net_avg_win | 75.5829 |
| net_avg_loss | -110.5751 |
| avg_hold_time_bars | 5.2047 |
| exposure | 0.0601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
