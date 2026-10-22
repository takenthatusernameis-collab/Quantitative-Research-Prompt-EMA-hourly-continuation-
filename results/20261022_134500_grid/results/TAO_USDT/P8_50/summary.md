# EMA Hourly Continuation — TAO/USDT P8_50

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1124 |
| net_profit_factor | 0.7083 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -5.1743 |
| sortino_ratio | -2.4397 |
| max_drawdown | 0.9515 |
| cagr | -0.6919 |
| net_avg_win | 42.3134 |
| net_avg_loss | -56.0318 |
| avg_hold_time_bars | 8.8345 |
| exposure | 0.4514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
