# EMA Hourly Continuation — ZBCN/USDT P50_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.9079 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0635 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.5593 |
| sortino_ratio | -0.1512 |
| max_drawdown | 0.2797 |
| cagr | -0.0708 |
| net_avg_win | 90.7538 |
| net_avg_loss | -107.0976 |
| avg_hold_time_bars | 13.8822 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
