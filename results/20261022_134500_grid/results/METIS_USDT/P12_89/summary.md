# EMA Hourly Continuation — METIS/USDT P12_89

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.5462 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.8145 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -5.4661 |
| sortino_ratio | -2.0555 |
| max_drawdown | 0.9193 |
| cagr | -0.6271 |
| net_avg_win | 35.4568 |
| net_avg_loss | -49.8454 |
| avg_hold_time_bars | 16.8659 |
| exposure | 0.5489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
