# EMA Hourly Continuation — DGB/USDT P12_50

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7401 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.5132 |
| sortino_ratio | -0.8826 |
| max_drawdown | 0.6555 |
| cagr | -0.3336 |
| net_avg_win | 62.1318 |
| net_avg_loss | -79.0870 |
| avg_hold_time_bars | 11.4222 |
| exposure | 0.3136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
