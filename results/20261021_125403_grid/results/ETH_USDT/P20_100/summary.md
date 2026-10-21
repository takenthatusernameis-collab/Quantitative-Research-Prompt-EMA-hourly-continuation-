# EMA Hourly Continuation — ETH/USDT P20_100

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0369 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.7910 |
| sortino_ratio | -0.4846 |
| max_drawdown | 0.4660 |
| cagr | -0.1986 |
| net_avg_win | 66.1443 |
| net_avg_loss | -93.3204 |
| avg_hold_time_bars | 27.3070 |
| exposure | 0.4406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
