# EMA Hourly Continuation — SWFTC/USDT P26_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -1.9732 |
| sortino_ratio | -0.5510 |
| max_drawdown | 0.4774 |
| cagr | -0.2235 |
| net_avg_win | 65.2039 |
| net_avg_loss | -82.7606 |
| avg_hold_time_bars | 18.4948 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
