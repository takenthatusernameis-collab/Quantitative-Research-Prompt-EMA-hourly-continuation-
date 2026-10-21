# EMA Hourly Continuation — SUPER/USDT P8_21

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -2.4835 |
| sortino_ratio | -0.8755 |
| max_drawdown | 0.6517 |
| cagr | -0.3320 |
| net_avg_win | 58.2103 |
| net_avg_loss | -79.6879 |
| avg_hold_time_bars | 5.4719 |
| exposure | 0.1507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
