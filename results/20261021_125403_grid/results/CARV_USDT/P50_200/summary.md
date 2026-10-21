# EMA Hourly Continuation — CARV/USDT P50_200

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.6144 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.7687 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -2.3244 |
| sortino_ratio | -0.5403 |
| max_drawdown | 0.4144 |
| cagr | -0.2191 |
| net_avg_win | 65.4926 |
| net_avg_loss | -83.8731 |
| avg_hold_time_bars | 28.8991 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
