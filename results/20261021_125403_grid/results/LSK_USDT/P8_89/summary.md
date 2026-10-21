# EMA Hourly Continuation — LSK/USDT P8_89

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.8130 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.5885 |
| sortino_ratio | -0.5222 |
| max_drawdown | 0.5299 |
| cagr | -0.2158 |
| net_avg_win | 74.1318 |
| net_avg_loss | -94.3516 |
| avg_hold_time_bars | 25.6015 |
| exposure | 0.6133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
