# EMA Hourly Continuation — BABYDOGE/USDT P20_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 34 |
| net_profit_factor | 1.3030 |
| net_win_rate | 0.5882 |
| gross_profit_factor | 1.4145 |
| gross_win_rate | 0.5882 |
| sharpe_ratio | 0.4996 |
| sortino_ratio | 0.0430 |
| max_drawdown | 0.0307 |
| cagr | 0.0178 |
| net_avg_win | 97.7662 |
| net_avg_loss | -107.1876 |
| avg_hold_time_bars | 25.5588 |
| exposure | 0.0393 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
