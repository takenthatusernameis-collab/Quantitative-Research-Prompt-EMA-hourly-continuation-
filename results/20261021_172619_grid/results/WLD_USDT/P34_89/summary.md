# EMA Hourly Continuation — WLD/USDT P34_89

**Symbol:** WLD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.9119 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.0988 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.4602 |
| sortino_ratio | -0.1290 |
| max_drawdown | 0.2338 |
| cagr | -0.0618 |
| net_avg_win | 76.9686 |
| net_avg_loss | -94.3593 |
| avg_hold_time_bars | 12.2573 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
