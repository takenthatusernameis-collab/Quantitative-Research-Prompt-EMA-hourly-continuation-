# EMA Hourly Continuation — CHR/USDT P21_89

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -4.7655 |
| sortino_ratio | -1.7959 |
| max_drawdown | 0.8927 |
| cagr | -0.5749 |
| net_avg_win | 39.2550 |
| net_avg_loss | -54.0804 |
| avg_hold_time_bars | 11.8072 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
