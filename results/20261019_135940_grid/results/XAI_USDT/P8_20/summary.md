# EMA Hourly Continuation — XAI/USDT P8_20

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1786 |
| net_profit_factor | 0.4776 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -11.8133 |
| sortino_ratio | -7.0483 |
| max_drawdown | 0.9998 |
| cagr | -0.9692 |
| net_avg_win | 12.1399 |
| net_avg_loss | -18.5283 |
| avg_hold_time_bars | 2.9104 |
| exposure | 0.2363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
