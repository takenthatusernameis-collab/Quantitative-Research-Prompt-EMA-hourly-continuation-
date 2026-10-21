# EMA Hourly Continuation — BTC/USDT P8_55

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5971 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -3.7982 |
| sortino_ratio | -1.3409 |
| max_drawdown | 0.8281 |
| cagr | -0.4594 |
| net_avg_win | 35.9425 |
| net_avg_loss | -58.9890 |
| avg_hold_time_bars | 17.3948 |
| exposure | 0.4794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
