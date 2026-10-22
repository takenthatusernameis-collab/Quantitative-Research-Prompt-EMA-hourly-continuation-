# EMA Hourly Continuation — ZBCN/USDT P12_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.8549 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1264 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -1.2901 |
| sortino_ratio | -0.4877 |
| max_drawdown | 0.4711 |
| cagr | -0.2088 |
| net_avg_win | 70.6577 |
| net_avg_loss | -93.3633 |
| avg_hold_time_bars | 18.7638 |
| exposure | 0.5990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
