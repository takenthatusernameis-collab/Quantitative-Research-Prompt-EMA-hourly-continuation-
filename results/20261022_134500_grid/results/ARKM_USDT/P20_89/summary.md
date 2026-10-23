# EMA Hourly Continuation — ARKM/USDT P20_89

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -4.8178 |
| sortino_ratio | -1.8748 |
| max_drawdown | 0.8956 |
| cagr | -0.5906 |
| net_avg_win | 33.7401 |
| net_avg_loss | -49.5117 |
| avg_hold_time_bars | 10.7997 |
| exposure | 0.3750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
