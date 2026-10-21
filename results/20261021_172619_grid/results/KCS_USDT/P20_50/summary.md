# EMA Hourly Continuation — KCS/USDT P20_50

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.3763 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.7233 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -6.6655 |
| sortino_ratio | -2.0606 |
| max_drawdown | 0.9135 |
| cagr | -0.6202 |
| net_avg_win | 30.7386 |
| net_avg_loss | -52.9823 |
| avg_hold_time_bars | 9.1648 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
