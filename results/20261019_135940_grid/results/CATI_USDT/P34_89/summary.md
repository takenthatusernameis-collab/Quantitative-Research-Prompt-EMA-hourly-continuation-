# EMA Hourly Continuation — CATI/USDT P34_89

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5890 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -5.3521 |
| sortino_ratio | -2.0921 |
| max_drawdown | 0.8837 |
| cagr | -0.6344 |
| net_avg_win | 42.1651 |
| net_avg_loss | -62.9345 |
| avg_hold_time_bars | 7.9608 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
