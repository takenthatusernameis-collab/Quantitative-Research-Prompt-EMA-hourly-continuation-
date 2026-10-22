# EMA Hourly Continuation — TAO/USDT P89_200

**Symbol:** TAO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6009 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.4499 |
| sortino_ratio | -0.9180 |
| max_drawdown | 0.6892 |
| cagr | -0.3678 |
| net_avg_win | 60.2268 |
| net_avg_loss | -86.9932 |
| avg_hold_time_bars | 10.1114 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
