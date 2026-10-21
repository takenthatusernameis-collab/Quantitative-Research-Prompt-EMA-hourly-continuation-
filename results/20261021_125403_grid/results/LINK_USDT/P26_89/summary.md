# EMA Hourly Continuation — LINK/USDT P26_89

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.2532 |
| sortino_ratio | -0.6589 |
| max_drawdown | 0.5485 |
| cagr | -0.2611 |
| net_avg_win | 68.9607 |
| net_avg_loss | -86.8893 |
| avg_hold_time_bars | 14.7095 |
| exposure | 0.2808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
