# EMA Hourly Continuation — SKL/USDT P50_144

**Symbol:** SKL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7430 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0337 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -2.1624 |
| sortino_ratio | -0.6726 |
| max_drawdown | 0.5775 |
| cagr | -0.2712 |
| net_avg_win | 65.2294 |
| net_avg_loss | -90.3910 |
| avg_hold_time_bars | 14.9499 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
