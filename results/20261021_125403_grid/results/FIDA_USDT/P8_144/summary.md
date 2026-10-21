# EMA Hourly Continuation — FIDA/USDT P8_144

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7367 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9176 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.8123 |
| sortino_ratio | -0.5300 |
| max_drawdown | 0.4698 |
| cagr | -0.2170 |
| net_avg_win | 62.8385 |
| net_avg_loss | -80.2117 |
| avg_hold_time_bars | 37.9858 |
| exposure | 0.7271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
