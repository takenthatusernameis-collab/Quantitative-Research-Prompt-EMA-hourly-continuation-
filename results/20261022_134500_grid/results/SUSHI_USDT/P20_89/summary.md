# EMA Hourly Continuation — SUSHI/USDT P20_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.6187 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -4.7047 |
| sortino_ratio | -1.7788 |
| max_drawdown | 0.8906 |
| cagr | -0.5774 |
| net_avg_win | 42.5330 |
| net_avg_loss | -59.4307 |
| avg_hold_time_bars | 11.8628 |
| exposure | 0.3913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
