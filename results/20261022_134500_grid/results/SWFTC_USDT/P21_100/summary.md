# EMA Hourly Continuation — SWFTC/USDT P21_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.4923 |
| net_win_rate | 0.4277 |
| gross_profit_factor | 0.7686 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -6.0329 |
| sortino_ratio | -2.2006 |
| max_drawdown | 0.9353 |
| cagr | -0.6628 |
| net_avg_win | 31.2529 |
| net_avg_loss | -47.4518 |
| avg_hold_time_bars | 12.6903 |
| exposure | 0.3911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
