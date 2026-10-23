# EMA Hourly Continuation — CFG/USDT P50_55

**Symbol:** CFG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.2399 |
| net_win_rate | 0.3534 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4031 |
| sharpe_ratio | -11.6758 |
| sortino_ratio | -4.9078 |
| max_drawdown | 0.9986 |
| cagr | -0.9266 |
| net_avg_win | 10.5390 |
| net_avg_loss | -24.0165 |
| avg_hold_time_bars | 1.9291 |
| exposure | 0.0742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
