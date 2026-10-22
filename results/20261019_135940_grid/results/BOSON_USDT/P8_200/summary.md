# EMA Hourly Continuation — BOSON/USDT P8_200

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7194 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9031 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -2.5136 |
| sortino_ratio | -0.7822 |
| max_drawdown | 0.6112 |
| cagr | -0.3052 |
| net_avg_win | 68.2819 |
| net_avg_loss | -81.8264 |
| avg_hold_time_bars | 33.0267 |
| exposure | 0.7296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
