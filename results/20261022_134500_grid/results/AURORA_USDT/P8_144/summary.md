# EMA Hourly Continuation — AURORA/USDT P8_144

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.1850 |
| sortino_ratio | -1.0380 |
| max_drawdown | 0.7287 |
| cagr | -0.3861 |
| net_avg_win | 58.5314 |
| net_avg_loss | -76.2503 |
| avg_hold_time_bars | 28.6667 |
| exposure | 0.6919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
