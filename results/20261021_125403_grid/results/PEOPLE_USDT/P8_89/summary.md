# EMA Hourly Continuation — PEOPLE/USDT P8_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7981 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -1.5582 |
| sortino_ratio | -0.4758 |
| max_drawdown | 0.4519 |
| cagr | -0.1977 |
| net_avg_win | 75.5619 |
| net_avg_loss | -88.7123 |
| avg_hold_time_bars | 31.8894 |
| exposure | 0.6652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
