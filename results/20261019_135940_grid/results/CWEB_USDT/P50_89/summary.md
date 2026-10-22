# EMA Hourly Continuation — CWEB/USDT P50_89

**Symbol:** CWEB/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.3965 |
| net_win_rate | 0.3504 |
| gross_profit_factor | 0.7776 |
| gross_win_rate | 0.3702 |
| sharpe_ratio | -9.5184 |
| sortino_ratio | -3.3304 |
| max_drawdown | 0.9901 |
| cagr | -0.8383 |
| net_avg_win | 30.6682 |
| net_avg_loss | -41.7268 |
| avg_hold_time_bars | 7.4182 |
| exposure | 0.2040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
