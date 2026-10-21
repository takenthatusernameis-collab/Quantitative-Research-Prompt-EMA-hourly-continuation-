# EMA Hourly Continuation — TWT/USDT P50_144

**Symbol:** TWT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.6649 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.3460 |
| sortino_ratio | -0.6235 |
| max_drawdown | 0.5458 |
| cagr | -0.2486 |
| net_avg_win | 61.5829 |
| net_avg_loss | -84.4377 |
| avg_hold_time_bars | 17.7890 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
