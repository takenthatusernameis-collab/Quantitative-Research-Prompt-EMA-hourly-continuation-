# EMA Hourly Continuation — ID/USDT P20_50

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -5.6986 |
| sortino_ratio | -2.4020 |
| max_drawdown | 0.9474 |
| cagr | -0.6860 |
| net_avg_win | 25.2302 |
| net_avg_loss | -42.4405 |
| avg_hold_time_bars | 5.8053 |
| exposure | 0.2362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
