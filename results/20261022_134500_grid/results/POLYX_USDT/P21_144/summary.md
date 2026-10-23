# EMA Hourly Continuation — POLYX/USDT P21_144

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.3458 |
| sortino_ratio | -0.7307 |
| max_drawdown | 0.6027 |
| cagr | -0.2919 |
| net_avg_win | 59.9559 |
| net_avg_loss | -82.8837 |
| avg_hold_time_bars | 23.6982 |
| exposure | 0.5246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
