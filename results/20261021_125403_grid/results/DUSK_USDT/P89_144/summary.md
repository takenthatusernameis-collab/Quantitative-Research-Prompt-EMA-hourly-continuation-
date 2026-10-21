# EMA Hourly Continuation — DUSK/USDT P89_144

**Symbol:** DUSK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.8598 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.0981 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.7702 |
| sortino_ratio | -0.1908 |
| max_drawdown | 0.2492 |
| cagr | -0.0856 |
| net_avg_win | 79.6720 |
| net_avg_loss | -102.5904 |
| avg_hold_time_bars | 6.9492 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
