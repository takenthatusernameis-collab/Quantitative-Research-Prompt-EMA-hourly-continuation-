# EMA Hourly Continuation — ATH/USDT P8_34

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.8403 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0643 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -1.4236 |
| sortino_ratio | -0.5387 |
| max_drawdown | 0.4912 |
| cagr | -0.2218 |
| net_avg_win | 70.0519 |
| net_avg_loss | -88.9417 |
| avg_hold_time_bars | 7.9599 |
| exposure | 0.2504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
