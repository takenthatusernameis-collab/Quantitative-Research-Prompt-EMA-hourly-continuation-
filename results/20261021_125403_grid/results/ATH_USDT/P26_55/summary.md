# EMA Hourly Continuation — ATH/USDT P26_55

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8790 |
| net_win_rate | 0.5319 |
| gross_profit_factor | 1.1341 |
| gross_win_rate | 0.5319 |
| sharpe_ratio | -0.7635 |
| sortino_ratio | -0.2208 |
| max_drawdown | 0.2439 |
| cagr | -0.0994 |
| net_avg_win | 79.3664 |
| net_avg_loss | -102.6018 |
| avg_hold_time_bars | 6.8457 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
