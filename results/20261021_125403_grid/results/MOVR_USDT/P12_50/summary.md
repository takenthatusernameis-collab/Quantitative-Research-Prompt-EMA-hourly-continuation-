# EMA Hourly Continuation — MOVR/USDT P12_50

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.9513 |
| sortino_ratio | -0.7284 |
| max_drawdown | 0.6124 |
| cagr | -0.2853 |
| net_avg_win | 59.4043 |
| net_avg_loss | -77.0199 |
| avg_hold_time_bars | 10.8643 |
| exposure | 0.3348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
