# EMA Hourly Continuation — PEPE/USDT P21_55

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -1.9121 |
| sortino_ratio | -0.5745 |
| max_drawdown | 0.4982 |
| cagr | -0.2319 |
| net_avg_win | 66.4267 |
| net_avg_loss | -84.2544 |
| avg_hold_time_bars | 9.0068 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
