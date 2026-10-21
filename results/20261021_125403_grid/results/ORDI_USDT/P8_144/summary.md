# EMA Hourly Continuation — ORDI/USDT P8_144

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8367 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -2.0461 |
| sortino_ratio | -0.5210 |
| max_drawdown | 0.4944 |
| cagr | -0.2134 |
| net_avg_win | 80.2796 |
| net_avg_loss | -90.3257 |
| avg_hold_time_bars | 52.5247 |
| exposure | 0.7735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
