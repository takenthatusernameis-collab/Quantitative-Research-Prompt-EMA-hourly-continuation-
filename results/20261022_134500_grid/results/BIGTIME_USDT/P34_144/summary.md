# EMA Hourly Continuation — BIGTIME/USDT P34_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.8266 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1338 |
| gross_win_rate | 0.5308 |
| sharpe_ratio | -1.3142 |
| sortino_ratio | -0.3977 |
| max_drawdown | 0.4175 |
| cagr | -0.1714 |
| net_avg_win | 75.0219 |
| net_avg_loss | -101.7869 |
| avg_hold_time_bars | 20.7335 |
| exposure | 0.4260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
