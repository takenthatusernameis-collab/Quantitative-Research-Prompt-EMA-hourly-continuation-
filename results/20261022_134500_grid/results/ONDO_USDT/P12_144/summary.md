# EMA Hourly Continuation — ONDO/USDT P12_144

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.7742 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0652 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.2030 |
| sortino_ratio | -0.7083 |
| max_drawdown | 0.6584 |
| cagr | -0.2868 |
| net_avg_win | 75.1366 |
| net_avg_loss | -97.0567 |
| avg_hold_time_bars | 26.1341 |
| exposure | 0.6201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
