# EMA Hourly Continuation — ETN/USDT P89_100

**Symbol:** ETN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.2288 |
| net_win_rate | 0.2968 |
| gross_profit_factor | 0.4873 |
| gross_win_rate | 0.3416 |
| sharpe_ratio | -12.2317 |
| sortino_ratio | -4.7878 |
| max_drawdown | 0.9956 |
| cagr | -0.9233 |
| net_avg_win | 16.4958 |
| net_avg_loss | -30.4419 |
| avg_hold_time_bars | 2.5373 |
| exposure | 0.0831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
