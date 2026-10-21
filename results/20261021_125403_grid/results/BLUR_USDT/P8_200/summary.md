# EMA Hourly Continuation — BLUR/USDT P8_200

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 1.1877 |
| net_win_rate | 0.5815 |
| gross_profit_factor | 1.3759 |
| gross_win_rate | 0.5815 |
| sharpe_ratio | 0.8309 |
| sortino_ratio | 0.1832 |
| max_drawdown | 0.0844 |
| cagr | 0.0767 |
| net_avg_win | 98.2420 |
| net_avg_loss | -114.9318 |
| avg_hold_time_bars | 81.6652 |
| exposure | 0.8389 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
