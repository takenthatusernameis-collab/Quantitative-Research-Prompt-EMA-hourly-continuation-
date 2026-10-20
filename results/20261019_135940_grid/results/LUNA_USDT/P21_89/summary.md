# EMA Hourly Continuation — LUNA/USDT P21_89

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 847 |
| net_profit_factor | 0.5308 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -7.0288 |
| sortino_ratio | -2.8709 |
| max_drawdown | 0.9729 |
| cagr | -0.7614 |
| net_avg_win | 29.5043 |
| net_avg_loss | -43.7371 |
| avg_hold_time_bars | 8.6765 |
| exposure | 0.3340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
