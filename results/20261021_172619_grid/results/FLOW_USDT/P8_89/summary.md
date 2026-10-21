# EMA Hourly Continuation — FLOW/USDT P8_89

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7658 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9448 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -1.7947 |
| sortino_ratio | -0.5696 |
| max_drawdown | 0.5243 |
| cagr | -0.2318 |
| net_avg_win | 65.4479 |
| net_avg_loss | -81.7442 |
| avg_hold_time_bars | 28.8182 |
| exposure | 0.6484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
