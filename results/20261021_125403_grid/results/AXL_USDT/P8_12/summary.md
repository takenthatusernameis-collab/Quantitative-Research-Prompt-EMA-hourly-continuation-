# EMA Hourly Continuation — AXL/USDT P8_12

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5398 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.7682 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -4.3455 |
| sortino_ratio | -1.2599 |
| max_drawdown | 0.7722 |
| cagr | -0.4420 |
| net_avg_win | 51.6315 |
| net_avg_loss | -69.7500 |
| avg_hold_time_bars | 4.1036 |
| exposure | 0.0771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
