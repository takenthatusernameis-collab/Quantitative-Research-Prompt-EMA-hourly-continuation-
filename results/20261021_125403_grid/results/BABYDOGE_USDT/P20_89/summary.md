# EMA Hourly Continuation — BABYDOGE/USDT P20_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 51 |
| net_profit_factor | 1.0422 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1149 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | 0.1135 |
| sortino_ratio | 0.0117 |
| max_drawdown | 0.0622 |
| cagr | 0.0041 |
| net_avg_win | 94.9490 |
| net_avg_loss | -102.4959 |
| avg_hold_time_bars | 63.0980 |
| exposure | 0.1456 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
