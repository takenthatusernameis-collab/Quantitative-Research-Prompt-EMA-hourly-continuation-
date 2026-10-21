# EMA Hourly Continuation — MASK/USDT P55_200

**Symbol:** MASK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7138 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.9290 |
| sortino_ratio | -0.5115 |
| max_drawdown | 0.4529 |
| cagr | -0.2093 |
| net_avg_win | 65.7411 |
| net_avg_loss | -89.4563 |
| avg_hold_time_bars | 25.1370 |
| exposure | 0.3919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
