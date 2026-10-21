# EMA Hourly Continuation — DUSK/USDT P20_200

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8448 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -0.8562 |
| sortino_ratio | -0.2041 |
| max_drawdown | 0.2639 |
| cagr | -0.0914 |
| net_avg_win | 85.0126 |
| net_avg_loss | -97.0905 |
| avg_hold_time_bars | 48.9642 |
| exposure | 0.6210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
