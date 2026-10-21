# EMA Hourly Continuation — TNSR/USDT P50_100

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7385 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9515 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -2.0137 |
| sortino_ratio | -0.5703 |
| max_drawdown | 0.5156 |
| cagr | -0.2312 |
| net_avg_win | 71.3002 |
| net_avg_loss | -91.3143 |
| avg_hold_time_bars | 8.9899 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
