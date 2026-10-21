# EMA Hourly Continuation — RENDER/USDT P26_100

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.8288 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0143 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.2133 |
| sortino_ratio | -0.3647 |
| max_drawdown | 0.3758 |
| cagr | -0.1564 |
| net_avg_win | 77.5618 |
| net_avg_loss | -96.0902 |
| avg_hold_time_bars | 15.4881 |
| exposure | 0.3098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
