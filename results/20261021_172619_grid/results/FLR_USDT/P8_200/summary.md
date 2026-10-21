# EMA Hourly Continuation — FLR/USDT P8_200

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.8038 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 0.9974 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.3210 |
| sortino_ratio | -0.3957 |
| max_drawdown | 0.3921 |
| cagr | -0.1680 |
| net_avg_win | 68.5382 |
| net_avg_loss | -86.8438 |
| avg_hold_time_bars | 35.4406 |
| exposure | 0.7056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
