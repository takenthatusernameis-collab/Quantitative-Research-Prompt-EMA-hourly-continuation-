# EMA Hourly Continuation — GRAM/USDT P20_89

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.4276 |
| net_win_rate | 0.4423 |
| gross_profit_factor | 0.8319 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -6.8314 |
| sortino_ratio | -2.6647 |
| max_drawdown | 0.9662 |
| cagr | -0.7353 |
| net_avg_win | 20.8831 |
| net_avg_loss | -38.7344 |
| avg_hold_time_bars | 10.2628 |
| exposure | 0.3639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
