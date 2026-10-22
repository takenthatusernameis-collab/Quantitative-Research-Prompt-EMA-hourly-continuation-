# EMA Hourly Continuation — ONDO/USDT P8_89

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9287 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.5045 |
| sortino_ratio | -1.7841 |
| max_drawdown | 0.8899 |
| cagr | -0.5763 |
| net_avg_win | 42.4578 |
| net_avg_loss | -57.6347 |
| avg_hold_time_bars | 16.3769 |
| exposure | 0.5925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
