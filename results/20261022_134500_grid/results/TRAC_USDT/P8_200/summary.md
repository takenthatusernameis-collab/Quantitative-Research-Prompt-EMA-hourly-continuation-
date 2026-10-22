# EMA Hourly Continuation — TRAC/USDT P8_200

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8057 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -3.7826 |
| sortino_ratio | -1.0956 |
| max_drawdown | 0.7381 |
| cagr | -0.4088 |
| net_avg_win | 52.8304 |
| net_avg_loss | -69.3050 |
| avg_hold_time_bars | 38.2791 |
| exposure | 0.7482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
