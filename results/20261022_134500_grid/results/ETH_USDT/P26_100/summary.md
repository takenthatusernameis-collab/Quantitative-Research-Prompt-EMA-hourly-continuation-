# EMA Hourly Continuation — ETH/USDT P26_100

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.4449 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -6.3037 |
| sortino_ratio | -2.1753 |
| max_drawdown | 0.9363 |
| cagr | -0.6627 |
| net_avg_win | 28.0615 |
| net_avg_loss | -50.5697 |
| avg_hold_time_bars | 13.1017 |
| exposure | 0.3573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
