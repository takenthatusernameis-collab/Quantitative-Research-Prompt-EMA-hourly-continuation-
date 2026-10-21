# EMA Hourly Continuation — INJ/USDT P8_50

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.8156 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -1.6325 |
| sortino_ratio | -0.5975 |
| max_drawdown | 0.5373 |
| cagr | -0.2418 |
| net_avg_win | 67.7502 |
| net_avg_loss | -83.3268 |
| avg_hold_time_bars | 14.3675 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
