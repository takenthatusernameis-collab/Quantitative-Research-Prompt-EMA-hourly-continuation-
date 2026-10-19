# EMA Hourly Continuation — CHZ/USDT P26_34

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1094 |
| net_profit_factor | 0.3144 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.8209 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -12.5005 |
| sortino_ratio | -5.9785 |
| max_drawdown | 0.9996 |
| cagr | -0.9549 |
| net_avg_win | 10.6098 |
| net_avg_loss | -22.0231 |
| avg_hold_time_bars | 2.0110 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
