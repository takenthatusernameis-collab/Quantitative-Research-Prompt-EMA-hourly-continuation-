# EMA Hourly Continuation — ETH/USDT P26_50

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.9030 |
| sortino_ratio | -0.7582 |
| max_drawdown | 0.5894 |
| cagr | -0.2926 |
| net_avg_win | 49.1894 |
| net_avg_loss | -80.4610 |
| avg_hold_time_bars | 7.7030 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
