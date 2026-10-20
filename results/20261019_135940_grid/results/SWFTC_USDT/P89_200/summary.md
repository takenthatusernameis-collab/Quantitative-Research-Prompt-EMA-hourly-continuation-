# EMA Hourly Continuation — SWFTC/USDT P89_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.4810 |
| net_win_rate | 0.4032 |
| gross_profit_factor | 0.7759 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -5.2358 |
| sortino_ratio | -1.5456 |
| max_drawdown | 0.8469 |
| cagr | -0.5236 |
| net_avg_win | 44.7359 |
| net_avg_loss | -62.8393 |
| avg_hold_time_bars | 10.1751 |
| exposure | 0.2007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
