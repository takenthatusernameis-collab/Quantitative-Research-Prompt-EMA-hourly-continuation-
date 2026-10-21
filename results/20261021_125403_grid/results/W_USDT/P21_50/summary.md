# EMA Hourly Continuation — W/USDT P21_50

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.8065 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.6746 |
| sortino_ratio | -0.5507 |
| max_drawdown | 0.5123 |
| cagr | -0.2244 |
| net_avg_win | 74.4452 |
| net_avg_loss | -93.0162 |
| avg_hold_time_bars | 7.3118 |
| exposure | 0.1748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
