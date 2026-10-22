# EMA Hourly Continuation — CGPT/USDT P50_89

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7808 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.5178 |
| sortino_ratio | -0.4031 |
| max_drawdown | 0.3782 |
| cagr | -0.1698 |
| net_avg_win | 77.2994 |
| net_avg_loss | -99.5797 |
| avg_hold_time_bars | 8.4257 |
| exposure | 0.1314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
