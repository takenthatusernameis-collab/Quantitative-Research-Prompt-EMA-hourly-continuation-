# EMA Hourly Continuation — WIF/USDT P34_55

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 1.0054 |
| net_win_rate | 0.5636 |
| gross_profit_factor | 1.2738 |
| gross_win_rate | 0.5636 |
| sharpe_ratio | 0.0827 |
| sortino_ratio | 0.0200 |
| max_drawdown | 0.2569 |
| cagr | 0.0032 |
| net_avg_win | 97.1641 |
| net_avg_loss | -124.8343 |
| avg_hold_time_bars | 5.6400 |
| exposure | 0.0705 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
