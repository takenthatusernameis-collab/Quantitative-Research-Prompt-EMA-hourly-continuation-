# EMA Hourly Continuation — ASTR/USDT P55_89

**Symbol:** ASTR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -5.5825 |
| sortino_ratio | -1.9544 |
| max_drawdown | 0.9145 |
| cagr | -0.6187 |
| net_avg_win | 27.7431 |
| net_avg_loss | -52.2535 |
| avg_hold_time_bars | 5.0616 |
| exposure | 0.1413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
