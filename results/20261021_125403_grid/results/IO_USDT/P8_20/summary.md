# EMA Hourly Continuation — IO/USDT P8_20

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.3978 |
| sortino_ratio | -0.4573 |
| max_drawdown | 0.4377 |
| cagr | -0.1906 |
| net_avg_win | 70.9472 |
| net_avg_loss | -91.1038 |
| avg_hold_time_bars | 5.3169 |
| exposure | 0.1251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
