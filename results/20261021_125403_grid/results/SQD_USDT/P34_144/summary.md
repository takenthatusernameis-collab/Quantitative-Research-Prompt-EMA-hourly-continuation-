# EMA Hourly Continuation — SQD/USDT P34_144

**Symbol:** SQD/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8429 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.0100 |
| sortino_ratio | -0.2791 |
| max_drawdown | 0.3100 |
| cagr | -0.1226 |
| net_avg_win | 81.5916 |
| net_avg_loss | -95.2039 |
| avg_hold_time_bars | 22.0360 |
| exposure | 0.3739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
