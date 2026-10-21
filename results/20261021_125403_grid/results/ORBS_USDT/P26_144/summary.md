# EMA Hourly Continuation — ORBS/USDT P26_144

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.1827 |
| sortino_ratio | -0.6402 |
| max_drawdown | 0.6026 |
| cagr | -0.2552 |
| net_avg_win | 73.9679 |
| net_avg_loss | -94.3138 |
| avg_hold_time_bars | 25.2955 |
| exposure | 0.4864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
