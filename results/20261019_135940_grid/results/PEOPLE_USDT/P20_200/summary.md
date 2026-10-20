# EMA Hourly Continuation — PEOPLE/USDT P20_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8316 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0766 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -1.0737 |
| sortino_ratio | -0.2938 |
| max_drawdown | 0.3645 |
| cagr | -0.1299 |
| net_avg_win | 76.5315 |
| net_avg_loss | -98.7519 |
| avg_hold_time_bars | 38.3631 |
| exposure | 0.6406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
