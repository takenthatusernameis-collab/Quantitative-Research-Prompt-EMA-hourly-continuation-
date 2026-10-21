# EMA Hourly Continuation — ENS/USDT P26_50

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8206 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1349 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -1.4124 |
| sortino_ratio | -0.4196 |
| max_drawdown | 0.4314 |
| cagr | -0.1760 |
| net_avg_win | 78.5954 |
| net_avg_loss | -107.2773 |
| avg_hold_time_bars | 6.6179 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
