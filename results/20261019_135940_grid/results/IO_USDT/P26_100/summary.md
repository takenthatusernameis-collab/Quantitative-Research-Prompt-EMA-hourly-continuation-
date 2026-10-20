# EMA Hourly Continuation — IO/USDT P26_100

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5927 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8339 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -4.4253 |
| sortino_ratio | -1.6786 |
| max_drawdown | 0.8515 |
| cagr | -0.5529 |
| net_avg_win | 39.5221 |
| net_avg_loss | -56.1061 |
| avg_hold_time_bars | 9.5679 |
| exposure | 0.3173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
