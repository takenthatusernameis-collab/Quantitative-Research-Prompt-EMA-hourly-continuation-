# EMA Hourly Continuation — SUSHI/USDT P21_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.3924 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -10.4232 |
| sortino_ratio | -5.0797 |
| max_drawdown | 0.9984 |
| cagr | -0.9220 |
| net_avg_win | 12.9212 |
| net_avg_loss | -24.1288 |
| avg_hold_time_bars | 2.5076 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
