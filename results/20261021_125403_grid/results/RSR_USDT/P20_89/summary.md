# EMA Hourly Continuation — RSR/USDT P20_89

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7995 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9672 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.5744 |
| sortino_ratio | -0.4939 |
| max_drawdown | 0.4721 |
| cagr | -0.2048 |
| net_avg_win | 73.6490 |
| net_avg_loss | -89.1062 |
| avg_hold_time_bars | 16.6992 |
| exposure | 0.3659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
