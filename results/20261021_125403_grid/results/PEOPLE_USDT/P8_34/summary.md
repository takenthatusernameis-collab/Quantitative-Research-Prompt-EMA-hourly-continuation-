# EMA Hourly Continuation — PEOPLE/USDT P8_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.7506 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.1224 |
| sortino_ratio | -1.2288 |
| max_drawdown | 0.7597 |
| cagr | -0.4313 |
| net_avg_win | 63.3057 |
| net_avg_loss | -74.9885 |
| avg_hold_time_bars | 8.5541 |
| exposure | 0.2969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
