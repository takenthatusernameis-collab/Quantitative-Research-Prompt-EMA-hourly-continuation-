# EMA Hourly Continuation — AUCTION/USDT P55_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5386 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.7973 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -4.2034 |
| sortino_ratio | -1.2264 |
| max_drawdown | 0.7833 |
| cagr | -0.4505 |
| net_avg_win | 47.3615 |
| net_avg_loss | -68.3585 |
| avg_hold_time_bars | 18.6219 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
