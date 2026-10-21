# EMA Hourly Continuation — CTC/USDT P55_200

**Symbol:** CTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9948 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.4466 |
| sortino_ratio | -0.3722 |
| max_drawdown | 0.4034 |
| cagr | -0.1579 |
| net_avg_win | 71.5338 |
| net_avg_loss | -93.7519 |
| avg_hold_time_bars | 21.6873 |
| exposure | 0.3184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
