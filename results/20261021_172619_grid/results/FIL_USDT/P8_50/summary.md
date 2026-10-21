# EMA Hourly Continuation — FIL/USDT P8_50

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0099 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.7998 |
| sortino_ratio | -0.6435 |
| max_drawdown | 0.5487 |
| cagr | -0.2573 |
| net_avg_win | 64.7465 |
| net_avg_loss | -82.6144 |
| avg_hold_time_bars | 15.7637 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
