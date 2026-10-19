# EMA Hourly Continuation — TAO/USDT P26_50

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.5398 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -6.7686 |
| sortino_ratio | -2.9344 |
| max_drawdown | 0.9746 |
| cagr | -0.7657 |
| net_avg_win | 25.7895 |
| net_avg_loss | -41.0940 |
| avg_hold_time_bars | 3.4311 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
