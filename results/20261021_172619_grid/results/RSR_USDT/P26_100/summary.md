# EMA Hourly Continuation — RSR/USDT P26_100

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8439 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0254 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.1579 |
| sortino_ratio | -0.3563 |
| max_drawdown | 0.3684 |
| cagr | -0.1533 |
| net_avg_win | 79.2451 |
| net_avg_loss | -95.9645 |
| avg_hold_time_bars | 15.2039 |
| exposure | 0.3186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
