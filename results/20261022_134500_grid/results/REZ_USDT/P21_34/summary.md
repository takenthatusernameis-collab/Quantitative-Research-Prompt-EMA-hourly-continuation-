# EMA Hourly Continuation — REZ/USDT P21_34

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 1.0631 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -8.2258 |
| sortino_ratio | -3.7837 |
| max_drawdown | 0.9912 |
| cagr | -0.8489 |
| net_avg_win | 28.5162 |
| net_avg_loss | -39.2776 |
| avg_hold_time_bars | 3.1000 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
