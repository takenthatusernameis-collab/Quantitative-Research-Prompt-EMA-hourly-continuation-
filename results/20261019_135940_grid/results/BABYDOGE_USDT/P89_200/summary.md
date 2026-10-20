# EMA Hourly Continuation — BABYDOGE/USDT P89_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 28 |
| net_profit_factor | 0.6882 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7439 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -0.6035 |
| sortino_ratio | -0.0448 |
| max_drawdown | 0.0602 |
| cagr | -0.0205 |
| net_avg_win | 93.6520 |
| net_avg_loss | -102.0675 |
| avg_hold_time_bars | 35.0714 |
| exposure | 0.0444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
