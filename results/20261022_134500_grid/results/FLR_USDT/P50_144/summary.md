# EMA Hourly Continuation — FLR/USDT P50_144

**Symbol:** FLR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.5399 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -5.1896 |
| sortino_ratio | -1.8309 |
| max_drawdown | 0.8930 |
| cagr | -0.5852 |
| net_avg_win | 37.1821 |
| net_avg_loss | -56.5823 |
| avg_hold_time_bars | 9.0851 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
