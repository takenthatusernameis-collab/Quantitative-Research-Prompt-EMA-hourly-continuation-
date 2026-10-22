# EMA Hourly Continuation — AKT/USDT P55_100

**Symbol:** AKT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -4.0558 |
| sortino_ratio | -1.4368 |
| max_drawdown | 0.8302 |
| cagr | -0.5031 |
| net_avg_win | 44.0136 |
| net_avg_loss | -67.6364 |
| avg_hold_time_bars | 5.0501 |
| exposure | 0.1467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
