# EMA Hourly Continuation — XDC/USDT P12_144

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0260 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.8620 |
| sortino_ratio | -0.5832 |
| max_drawdown | 0.4908 |
| cagr | -0.2348 |
| net_avg_win | 65.6483 |
| net_avg_loss | -88.0511 |
| avg_hold_time_bars | 24.3243 |
| exposure | 0.5285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
