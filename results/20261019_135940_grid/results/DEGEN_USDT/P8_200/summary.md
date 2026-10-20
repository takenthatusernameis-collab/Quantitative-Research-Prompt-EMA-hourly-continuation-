# EMA Hourly Continuation — DEGEN/USDT P8_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.2094 |
| sortino_ratio | -0.5752 |
| max_drawdown | 0.5233 |
| cagr | -0.2402 |
| net_avg_win | 71.8524 |
| net_avg_loss | -90.9167 |
| avg_hold_time_bars | 52.2157 |
| exposure | 0.8154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
