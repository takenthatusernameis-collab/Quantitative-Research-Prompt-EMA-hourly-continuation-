# EMA Hourly Continuation — MLK/USDT P26_89

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.2984 |
| net_win_rate | 0.3009 |
| gross_profit_factor | 0.5549 |
| gross_win_rate | 0.3100 |
| sharpe_ratio | -12.6888 |
| sortino_ratio | -5.6716 |
| max_drawdown | 0.9993 |
| cagr | -0.9431 |
| net_avg_win | 14.3122 |
| net_avg_loss | -20.6427 |
| avg_hold_time_bars | 6.8946 |
| exposure | 0.3080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
