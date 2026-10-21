# EMA Hourly Continuation — TURBO/USDT P8_55

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.8086 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9756 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.9655 |
| sortino_ratio | -0.7339 |
| max_drawdown | 0.5594 |
| cagr | -0.2877 |
| net_avg_win | 76.6866 |
| net_avg_loss | -91.5717 |
| avg_hold_time_bars | 13.6474 |
| exposure | 0.4244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
