# EMA Hourly Continuation — ZRO/USDT P8_89

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.9694 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1226 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.1438 |
| sortino_ratio | -0.0469 |
| max_drawdown | 0.1723 |
| cagr | -0.0302 |
| net_avg_win | 86.7373 |
| net_avg_loss | -101.5655 |
| avg_hold_time_bars | 26.1582 |
| exposure | 0.6069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
