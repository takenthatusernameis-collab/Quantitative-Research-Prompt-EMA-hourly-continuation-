# EMA Hourly Continuation — AEVO/USDT P8_144

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8930 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.6382 |
| sortino_ratio | -0.1647 |
| max_drawdown | 0.2906 |
| cagr | -0.0762 |
| net_avg_win | 90.5649 |
| net_avg_loss | -106.5218 |
| avg_hold_time_bars | 53.4663 |
| exposure | 0.7887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
