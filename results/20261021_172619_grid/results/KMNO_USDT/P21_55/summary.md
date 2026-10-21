# EMA Hourly Continuation — KMNO/USDT P21_55

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.6145 |
| sortino_ratio | -0.8238 |
| max_drawdown | 0.6276 |
| cagr | -0.3162 |
| net_avg_win | 56.2850 |
| net_avg_loss | -75.8467 |
| avg_hold_time_bars | 8.6258 |
| exposure | 0.1916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
