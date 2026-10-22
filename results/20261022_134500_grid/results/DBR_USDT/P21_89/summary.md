# EMA Hourly Continuation — DBR/USDT P21_89

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.4656 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.7786 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -5.7625 |
| sortino_ratio | -2.0355 |
| max_drawdown | 0.8690 |
| cagr | -0.6328 |
| net_avg_win | 34.1437 |
| net_avg_loss | -56.2739 |
| avg_hold_time_bars | 13.5717 |
| exposure | 0.3928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
