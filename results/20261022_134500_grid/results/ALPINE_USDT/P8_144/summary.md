# EMA Hourly Continuation — ALPINE/USDT P8_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.8013 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0820 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.0851 |
| sortino_ratio | -0.2484 |
| max_drawdown | 0.3140 |
| cagr | -0.1101 |
| net_avg_win | 77.0178 |
| net_avg_loss | -101.4536 |
| avg_hold_time_bars | 71.2394 |
| exposure | 0.8387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
