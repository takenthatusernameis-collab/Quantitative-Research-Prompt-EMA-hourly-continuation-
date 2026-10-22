# EMA Hourly Continuation — AIOZ/USDT P50_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 1.0120 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -3.2877 |
| sortino_ratio | -1.0983 |
| max_drawdown | 0.7406 |
| cagr | -0.4077 |
| net_avg_win | 57.5181 |
| net_avg_loss | -79.2520 |
| avg_hold_time_bars | 11.2000 |
| exposure | 0.2851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
