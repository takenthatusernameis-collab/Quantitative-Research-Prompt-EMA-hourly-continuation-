# EMA Hourly Continuation — MOVR/USDT P50_144

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8702 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.1820 |
| sortino_ratio | -0.6131 |
| max_drawdown | 0.5366 |
| cagr | -0.2458 |
| net_avg_win | 64.3203 |
| net_avg_loss | -80.6822 |
| avg_hold_time_bars | 14.7487 |
| exposure | 0.2615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
