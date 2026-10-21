# EMA Hourly Continuation — QNT/USDT P100_144

**Symbol:** QNT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.5861 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -2.7631 |
| sortino_ratio | -0.6286 |
| max_drawdown | 0.5249 |
| cagr | -0.2500 |
| net_avg_win | 62.8133 |
| net_avg_loss | -90.7414 |
| avg_hold_time_bars | 6.3202 |
| exposure | 0.0727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
