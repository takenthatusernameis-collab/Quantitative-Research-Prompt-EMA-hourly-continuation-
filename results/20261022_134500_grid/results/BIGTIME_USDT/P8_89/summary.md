# EMA Hourly Continuation — BIGTIME/USDT P8_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.7242 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 1.0054 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.6736 |
| sortino_ratio | -0.9338 |
| max_drawdown | 0.6868 |
| cagr | -0.3565 |
| net_avg_win | 58.3507 |
| net_avg_loss | -77.2489 |
| avg_hold_time_bars | 23.8266 |
| exposure | 0.6653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
