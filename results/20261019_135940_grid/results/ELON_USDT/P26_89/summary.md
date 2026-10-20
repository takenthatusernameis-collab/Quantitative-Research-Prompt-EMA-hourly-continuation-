# EMA Hourly Continuation — ELON/USDT P26_89

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.4482 |
| net_win_rate | 0.4189 |
| gross_profit_factor | 0.7328 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -6.4374 |
| sortino_ratio | -2.4246 |
| max_drawdown | 0.9487 |
| cagr | -0.6878 |
| net_avg_win | 25.8745 |
| net_avg_loss | -41.6197 |
| avg_hold_time_bars | 8.9605 |
| exposure | 0.2888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
