# EMA Hourly Continuation — SYN/USDT P20_89

**Symbol:** SYN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6662 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -3.5107 |
| sortino_ratio | -1.2900 |
| max_drawdown | 0.8007 |
| cagr | -0.4613 |
| net_avg_win | 48.2695 |
| net_avg_loss | -66.5364 |
| avg_hold_time_bars | 13.1395 |
| exposure | 0.4067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
