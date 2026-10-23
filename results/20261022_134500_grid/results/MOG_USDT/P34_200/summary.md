# EMA Hourly Continuation — MOG/USDT P34_200

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6931 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -2.2234 |
| sortino_ratio | -0.6032 |
| max_drawdown | 0.4953 |
| cagr | -0.2450 |
| net_avg_win | 68.4068 |
| net_avg_loss | -86.0870 |
| avg_hold_time_bars | 29.4599 |
| exposure | 0.4935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
