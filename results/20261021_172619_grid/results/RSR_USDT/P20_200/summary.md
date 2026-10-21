# EMA Hourly Continuation — RSR/USDT P20_200

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8771 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0128 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.7116 |
| sortino_ratio | -0.1838 |
| max_drawdown | 0.2270 |
| cagr | -0.0840 |
| net_avg_win | 86.0508 |
| net_avg_loss | -99.9363 |
| avg_hold_time_bars | 41.0585 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
