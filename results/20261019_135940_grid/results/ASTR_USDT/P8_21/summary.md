# EMA Hourly Continuation — ASTR/USDT P8_21

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.3918 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -10.7771 |
| sortino_ratio | -5.9019 |
| max_drawdown | 0.9994 |
| cagr | -0.9476 |
| net_avg_win | 9.6542 |
| net_avg_loss | -19.6573 |
| avg_hold_time_bars | 3.6866 |
| exposure | 0.2507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
