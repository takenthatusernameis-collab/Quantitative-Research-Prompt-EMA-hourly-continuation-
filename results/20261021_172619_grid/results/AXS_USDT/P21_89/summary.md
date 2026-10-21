# EMA Hourly Continuation — AXS/USDT P21_89

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.8586 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0969 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.9825 |
| sortino_ratio | -0.3064 |
| max_drawdown | 0.3291 |
| cagr | -0.1341 |
| net_avg_win | 74.8734 |
| net_avg_loss | -96.1561 |
| avg_hold_time_bars | 16.7410 |
| exposure | 0.3568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
