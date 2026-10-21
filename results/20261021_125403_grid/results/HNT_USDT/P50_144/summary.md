# EMA Hourly Continuation — HNT/USDT P50_144

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -2.4300 |
| sortino_ratio | -0.6683 |
| max_drawdown | 0.5838 |
| cagr | -0.2648 |
| net_avg_win | 55.0256 |
| net_avg_loss | -71.1864 |
| avg_hold_time_bars | 16.0265 |
| exposure | 0.2746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
