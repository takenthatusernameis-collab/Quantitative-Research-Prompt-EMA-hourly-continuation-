# EMA Hourly Continuation — ALEX/USDT P20_55

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.5291 |
| net_win_rate | 0.3977 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4168 |
| sharpe_ratio | -7.5061 |
| sortino_ratio | -2.9508 |
| max_drawdown | 0.9763 |
| cagr | -0.7693 |
| net_avg_win | 34.9985 |
| net_avg_loss | -43.6776 |
| avg_hold_time_bars | 8.6112 |
| exposure | 0.3080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
