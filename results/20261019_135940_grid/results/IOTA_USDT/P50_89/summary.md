# EMA Hourly Continuation — IOTA/USDT P50_89

**Symbol:** IOTA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.4742 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -6.0438 |
| sortino_ratio | -2.2094 |
| max_drawdown | 0.9398 |
| cagr | -0.6603 |
| net_avg_win | 27.8755 |
| net_avg_loss | -48.1142 |
| avg_hold_time_bars | 4.7452 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
