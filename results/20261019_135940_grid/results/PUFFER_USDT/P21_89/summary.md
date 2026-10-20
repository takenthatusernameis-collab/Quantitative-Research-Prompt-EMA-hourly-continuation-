# EMA Hourly Continuation — PUFFER/USDT P21_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7769 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0893 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -1.8953 |
| sortino_ratio | -0.6775 |
| max_drawdown | 0.4780 |
| cagr | -0.2749 |
| net_avg_win | 62.9515 |
| net_avg_loss | -86.9545 |
| avg_hold_time_bars | 14.3471 |
| exposure | 0.4141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
