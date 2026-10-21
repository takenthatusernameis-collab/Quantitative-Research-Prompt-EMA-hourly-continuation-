# EMA Hourly Continuation — BNB/USDT P12_26

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5723 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0495 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -3.4331 |
| sortino_ratio | -0.9588 |
| max_drawdown | 0.6808 |
| cagr | -0.3537 |
| net_avg_win | 47.8984 |
| net_avg_loss | -84.1486 |
| avg_hold_time_bars | 5.8437 |
| exposure | 0.0985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
