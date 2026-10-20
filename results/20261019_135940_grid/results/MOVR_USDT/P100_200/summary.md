# EMA Hourly Continuation — MOVR/USDT P100_200

**Symbol:** MOVR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5647 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -3.5950 |
| sortino_ratio | -1.0362 |
| max_drawdown | 0.7128 |
| cagr | -0.3866 |
| net_avg_win | 48.2606 |
| net_avg_loss | -71.8522 |
| avg_hold_time_bars | 10.5817 |
| exposure | 0.2001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
