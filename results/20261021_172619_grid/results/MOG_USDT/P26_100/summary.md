# EMA Hourly Continuation — MOG/USDT P26_100

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7728 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -1.6744 |
| sortino_ratio | -0.5058 |
| max_drawdown | 0.4707 |
| cagr | -0.2085 |
| net_avg_win | 71.3743 |
| net_avg_loss | -85.8535 |
| avg_hold_time_bars | 14.6667 |
| exposure | 0.2997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
