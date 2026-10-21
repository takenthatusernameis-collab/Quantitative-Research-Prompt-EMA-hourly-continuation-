# EMA Hourly Continuation — PYTH/USDT P100_200

**Symbol:** PYTH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.8177 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -0.9035 |
| sortino_ratio | -0.2032 |
| max_drawdown | 0.2797 |
| cagr | -0.0905 |
| net_avg_win | 76.6677 |
| net_avg_loss | -95.2915 |
| avg_hold_time_bars | 13.1992 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
