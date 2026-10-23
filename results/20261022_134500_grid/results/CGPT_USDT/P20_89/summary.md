# EMA Hourly Continuation — CGPT/USDT P20_89

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.6291 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -4.0464 |
| sortino_ratio | -1.5009 |
| max_drawdown | 0.8438 |
| cagr | -0.5166 |
| net_avg_win | 42.7307 |
| net_avg_loss | -61.4625 |
| avg_hold_time_bars | 11.6063 |
| exposure | 0.3698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
