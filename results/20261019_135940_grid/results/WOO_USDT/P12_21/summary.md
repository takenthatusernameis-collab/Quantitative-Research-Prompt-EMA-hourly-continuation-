# EMA Hourly Continuation — WOO/USDT P12_21

**Symbol:** WOO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1445 |
| net_profit_factor | 0.3498 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.8306 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -12.6335 |
| sortino_ratio | -6.8341 |
| max_drawdown | 0.9998 |
| cagr | -0.9687 |
| net_avg_win | 9.3064 |
| net_avg_loss | -17.7364 |
| avg_hold_time_bars | 2.5806 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
