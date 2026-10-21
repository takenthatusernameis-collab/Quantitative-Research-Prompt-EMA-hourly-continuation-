# EMA Hourly Continuation — SUPER/USDT P100_200

**Symbol:** SUPER/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.7735 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9740 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.2840 |
| sortino_ratio | -0.2945 |
| max_drawdown | 0.3421 |
| cagr | -0.1277 |
| net_avg_win | 77.4604 |
| net_avg_loss | -98.6020 |
| avg_hold_time_bars | 11.7054 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
