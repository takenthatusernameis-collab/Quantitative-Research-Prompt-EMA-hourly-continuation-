# EMA Hourly Continuation — WIF/USDT P8_144

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9180 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.6719 |
| sortino_ratio | -0.8525 |
| max_drawdown | 0.6518 |
| cagr | -0.3305 |
| net_avg_win | 56.7070 |
| net_avg_loss | -74.8298 |
| avg_hold_time_bars | 31.4297 |
| exposure | 0.7315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
