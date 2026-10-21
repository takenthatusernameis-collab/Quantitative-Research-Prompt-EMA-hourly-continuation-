# EMA Hourly Continuation — MANTA/USDT P8_26

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.7354 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9686 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.1393 |
| sortino_ratio | -1.2386 |
| max_drawdown | 0.7634 |
| cagr | -0.4340 |
| net_avg_win | 57.2945 |
| net_avg_loss | -73.1485 |
| avg_hold_time_bars | 6.7139 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
