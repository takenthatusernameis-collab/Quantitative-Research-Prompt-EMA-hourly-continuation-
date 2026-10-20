# EMA Hourly Continuation — AURORA/USDT P8_12

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1611 |
| net_profit_factor | 0.2476 |
| net_win_rate | 0.2955 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.3731 |
| sharpe_ratio | -19.7591 |
| sortino_ratio | -11.8401 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 6.9146 |
| net_avg_loss | -11.7104 |
| avg_hold_time_bars | 2.3402 |
| exposure | 0.1714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
