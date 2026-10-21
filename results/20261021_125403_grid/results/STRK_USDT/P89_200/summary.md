# EMA Hourly Continuation — STRK/USDT P89_200

**Symbol:** STRK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8271 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9917 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9520 |
| sortino_ratio | -0.2273 |
| max_drawdown | 0.2755 |
| cagr | -0.1008 |
| net_avg_win | 80.6225 |
| net_avg_loss | -97.4759 |
| avg_hold_time_bars | 16.3201 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
