# EMA Hourly Continuation — WEMIX/USDT P20_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.5635 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.6924 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -3.3637 |
| sortino_ratio | -0.8538 |
| max_drawdown | 0.6338 |
| cagr | -0.3269 |
| net_avg_win | 61.6071 |
| net_avg_loss | -74.7789 |
| avg_hold_time_bars | 44.0800 |
| exposure | 0.6512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
