# EMA Hourly Continuation — FIDA/USDT P12_50

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.5311 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -6.1775 |
| sortino_ratio | -2.7518 |
| max_drawdown | 0.9650 |
| cagr | -0.7332 |
| net_avg_win | 24.0034 |
| net_avg_loss | -37.3227 |
| avg_hold_time_bars | 8.9443 |
| exposure | 0.4072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
