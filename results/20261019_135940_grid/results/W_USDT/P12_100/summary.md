# EMA Hourly Continuation — W/USDT P12_100

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.8307 |
| net_win_rate | 0.5381 |
| gross_profit_factor | 1.1589 |
| gross_win_rate | 0.5429 |
| sharpe_ratio | -1.3688 |
| sortino_ratio | -0.4804 |
| max_drawdown | 0.5327 |
| cagr | -0.2076 |
| net_avg_win | 65.4106 |
| net_avg_loss | -91.7250 |
| avg_hold_time_bars | 21.2885 |
| exposure | 0.5970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
