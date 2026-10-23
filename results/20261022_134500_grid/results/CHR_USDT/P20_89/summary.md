# EMA Hourly Continuation — CHR/USDT P20_89

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.7837 |
| sortino_ratio | -1.8019 |
| max_drawdown | 0.8920 |
| cagr | -0.5760 |
| net_avg_win | 39.8954 |
| net_avg_loss | -54.2821 |
| avg_hold_time_bars | 12.1181 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
