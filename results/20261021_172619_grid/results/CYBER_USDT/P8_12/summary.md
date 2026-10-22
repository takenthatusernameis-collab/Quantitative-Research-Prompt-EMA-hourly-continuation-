# EMA Hourly Continuation — CYBER/USDT P8_12

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7988 |
| net_win_rate | 0.5446 |
| gross_profit_factor | 1.1972 |
| gross_win_rate | 0.5470 |
| sharpe_ratio | -1.4651 |
| sortino_ratio | -0.4322 |
| max_drawdown | 0.4211 |
| cagr | -0.1792 |
| net_avg_win | 68.6866 |
| net_avg_loss | -102.8162 |
| avg_hold_time_bars | 4.9277 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
