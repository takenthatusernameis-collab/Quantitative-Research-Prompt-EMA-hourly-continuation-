# EMA Hourly Continuation — XAI/USDT P89_100

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.6579 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9365 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.4934 |
| sortino_ratio | -0.2442 |
| max_drawdown | 0.2994 |
| cagr | -0.1056 |
| net_avg_win | 74.5905 |
| net_avg_loss | -106.6133 |
| avg_hold_time_bars | 5.0538 |
| exposure | 0.0299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
