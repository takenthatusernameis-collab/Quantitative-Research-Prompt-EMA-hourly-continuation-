# EMA Hourly Continuation — ALGO/USDT P8_21

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5403 |
| gross_profit_factor | 1.1863 |
| gross_win_rate | 0.5403 |
| sharpe_ratio | -1.2054 |
| sortino_ratio | -0.3890 |
| max_drawdown | 0.4237 |
| cagr | -0.1646 |
| net_avg_win | 77.4096 |
| net_avg_loss | -106.9284 |
| avg_hold_time_bars | 5.4153 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
