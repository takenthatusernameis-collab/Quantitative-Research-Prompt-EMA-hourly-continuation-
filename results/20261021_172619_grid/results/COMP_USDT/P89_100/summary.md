# EMA Hourly Continuation — COMP/USDT P89_100

**Symbol:** COMP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.5305 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.8943 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.1295 |
| sortino_ratio | -0.3648 |
| max_drawdown | 0.3459 |
| cagr | -0.1523 |
| net_avg_win | 56.4351 |
| net_avg_loss | -99.1016 |
| avg_hold_time_bars | 4.0284 |
| exposure | 0.0258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
