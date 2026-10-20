# EMA Hourly Continuation — SQD/USDT P34_200

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0420 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -1.3326 |
| sortino_ratio | -0.3862 |
| max_drawdown | 0.3818 |
| cagr | -0.1642 |
| net_avg_win | 72.0494 |
| net_avg_loss | -92.7406 |
| avg_hold_time_bars | 25.7884 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
