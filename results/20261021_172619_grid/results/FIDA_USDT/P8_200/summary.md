# EMA Hourly Continuation — FIDA/USDT P8_200

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.8069 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.1073 |
| sortino_ratio | -0.2821 |
| max_drawdown | 0.2943 |
| cagr | -0.1227 |
| net_avg_win | 73.9261 |
| net_avg_loss | -91.0423 |
| avg_hold_time_bars | 54.0972 |
| exposure | 0.7809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
