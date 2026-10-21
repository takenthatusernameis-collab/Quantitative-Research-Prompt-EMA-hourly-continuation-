# EMA Hourly Continuation — CPOOL/USDT P34_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -1.6812 |
| sortino_ratio | -0.4908 |
| max_drawdown | 0.4683 |
| cagr | -0.2032 |
| net_avg_win | 69.5141 |
| net_avg_loss | -85.4571 |
| avg_hold_time_bars | 8.2291 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
