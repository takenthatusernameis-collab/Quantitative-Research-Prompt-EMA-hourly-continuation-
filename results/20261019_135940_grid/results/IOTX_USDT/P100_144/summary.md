# EMA Hourly Continuation — IOTX/USDT P100_144

**Symbol:** IOTX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.4440 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -5.6737 |
| sortino_ratio | -1.8911 |
| max_drawdown | 0.9069 |
| cagr | -0.6067 |
| net_avg_win | 28.5303 |
| net_avg_loss | -53.6573 |
| avg_hold_time_bars | 3.8237 |
| exposure | 0.0966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
