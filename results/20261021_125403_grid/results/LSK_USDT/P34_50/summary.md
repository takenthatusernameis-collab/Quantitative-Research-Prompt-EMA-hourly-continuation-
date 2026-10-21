# EMA Hourly Continuation — LSK/USDT P34_50

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -3.3291 |
| sortino_ratio | -0.9650 |
| max_drawdown | 0.6752 |
| cagr | -0.3587 |
| net_avg_win | 51.6937 |
| net_avg_loss | -82.4245 |
| avg_hold_time_bars | 5.3784 |
| exposure | 0.0995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
