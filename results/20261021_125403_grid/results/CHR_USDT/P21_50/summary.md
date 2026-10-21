# EMA Hourly Continuation — CHR/USDT P21_50

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.9712 |
| sortino_ratio | -0.9956 |
| max_drawdown | 0.6919 |
| cagr | -0.3659 |
| net_avg_win | 55.6987 |
| net_avg_loss | -71.8137 |
| avg_hold_time_bars | 7.2775 |
| exposure | 0.1828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
