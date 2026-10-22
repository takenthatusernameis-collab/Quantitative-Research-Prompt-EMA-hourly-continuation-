# EMA Hourly Continuation — DOGE/USDT P8_50

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1170 |
| net_profit_factor | 0.4801 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -7.9922 |
| sortino_ratio | -3.8095 |
| max_drawdown | 0.9919 |
| cagr | -0.8524 |
| net_avg_win | 17.4481 |
| net_avg_loss | -29.5788 |
| avg_hold_time_bars | 7.6615 |
| exposure | 0.4075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
