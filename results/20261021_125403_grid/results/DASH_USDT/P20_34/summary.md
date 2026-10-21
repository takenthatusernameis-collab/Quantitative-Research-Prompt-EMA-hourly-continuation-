# EMA Hourly Continuation — DASH/USDT P20_34

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6008 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.5267 |
| sortino_ratio | -0.6088 |
| max_drawdown | 0.5187 |
| cagr | -0.2431 |
| net_avg_win | 56.9237 |
| net_avg_loss | -84.0144 |
| avg_hold_time_bars | 5.4346 |
| exposure | 0.0699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
