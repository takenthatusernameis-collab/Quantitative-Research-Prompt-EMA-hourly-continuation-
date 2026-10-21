# EMA Hourly Continuation — ATOM/USDT P26_200

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.8186 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -0.9658 |
| sortino_ratio | -0.2386 |
| max_drawdown | 0.3151 |
| cagr | -0.1055 |
| net_avg_win | 73.4596 |
| net_avg_loss | -91.5677 |
| avg_hold_time_bars | 41.5152 |
| exposure | 0.5605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
