# EMA Hourly Continuation — KSM/USDT P20_144

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5714 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -3.8701 |
| sortino_ratio | -1.0933 |
| max_drawdown | 0.7467 |
| cagr | -0.4167 |
| net_avg_win | 54.0342 |
| net_avg_loss | -74.5950 |
| avg_hold_time_bars | 31.7614 |
| exposure | 0.5991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
