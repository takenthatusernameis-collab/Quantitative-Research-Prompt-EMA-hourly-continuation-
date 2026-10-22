# EMA Hourly Continuation — AVAX/USDT P8_50

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.5548 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -7.1734 |
| sortino_ratio | -3.3415 |
| max_drawdown | 0.9848 |
| cagr | -0.8045 |
| net_avg_win | 24.7077 |
| net_avg_loss | -36.4507 |
| avg_hold_time_bars | 9.0998 |
| exposure | 0.4558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
