# EMA Hourly Continuation — ORBS/USDT P26_100

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.5812 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -6.1932 |
| sortino_ratio | -2.3192 |
| max_drawdown | 0.9475 |
| cagr | -0.6805 |
| net_avg_win | 41.9480 |
| net_avg_loss | -56.4370 |
| avg_hold_time_bars | 12.1055 |
| exposure | 0.3912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
