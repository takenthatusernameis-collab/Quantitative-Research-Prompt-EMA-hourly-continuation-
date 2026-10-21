# EMA Hourly Continuation — KAVA/USDT P34_200

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.7744 |
| sortino_ratio | -0.4625 |
| max_drawdown | 0.4622 |
| cagr | -0.1956 |
| net_avg_win | 77.4915 |
| net_avg_loss | -101.9542 |
| avg_hold_time_bars | 32.0059 |
| exposure | 0.4903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
