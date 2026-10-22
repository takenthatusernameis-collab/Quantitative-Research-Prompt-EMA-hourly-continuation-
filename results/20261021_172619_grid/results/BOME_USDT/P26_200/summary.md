# EMA Hourly Continuation — BOME/USDT P26_200

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.9895 |
| net_win_rate | 0.5357 |
| gross_profit_factor | 1.1393 |
| gross_win_rate | 0.5357 |
| sharpe_ratio | 0.0027 |
| sortino_ratio | 0.0007 |
| max_drawdown | 0.2260 |
| cagr | -0.0052 |
| net_avg_win | 82.0943 |
| net_avg_loss | -95.7303 |
| avg_hold_time_bars | 44.3750 |
| exposure | 0.5648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
