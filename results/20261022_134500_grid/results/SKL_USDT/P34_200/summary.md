# EMA Hourly Continuation — SKL/USDT P34_200

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6377 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.6379 |
| sortino_ratio | -0.6911 |
| max_drawdown | 0.6101 |
| cagr | -0.2814 |
| net_avg_win | 60.9015 |
| net_avg_loss | -83.6875 |
| avg_hold_time_bars | 35.3410 |
| exposure | 0.5606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
