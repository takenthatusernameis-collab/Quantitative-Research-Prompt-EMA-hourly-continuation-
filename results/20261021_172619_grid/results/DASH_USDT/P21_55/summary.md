# EMA Hourly Continuation — DASH/USDT P21_55

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.2956 |
| sortino_ratio | -0.7100 |
| max_drawdown | 0.5623 |
| cagr | -0.2777 |
| net_avg_win | 58.8915 |
| net_avg_loss | -80.4551 |
| avg_hold_time_bars | 9.0043 |
| exposure | 0.1907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
