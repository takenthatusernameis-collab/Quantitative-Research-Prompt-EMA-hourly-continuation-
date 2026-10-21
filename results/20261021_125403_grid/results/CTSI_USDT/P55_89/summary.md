# EMA Hourly Continuation — CTSI/USDT P55_89

**Symbol:** CTSI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6395 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.8820 |
| sortino_ratio | -0.8488 |
| max_drawdown | 0.6254 |
| cagr | -0.3217 |
| net_avg_win | 54.4029 |
| net_avg_loss | -78.5022 |
| avg_hold_time_bars | 6.9622 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
