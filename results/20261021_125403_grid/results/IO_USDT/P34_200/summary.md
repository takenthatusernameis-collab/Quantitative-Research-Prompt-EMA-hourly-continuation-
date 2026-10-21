# EMA Hourly Continuation — IO/USDT P34_200

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.9210 |
| net_win_rate | 0.5175 |
| gross_profit_factor | 1.0669 |
| gross_win_rate | 0.5175 |
| sharpe_ratio | -0.4090 |
| sortino_ratio | -0.1027 |
| max_drawdown | 0.1461 |
| cagr | -0.0499 |
| net_avg_win | 89.5761 |
| net_avg_loss | -104.3041 |
| avg_hold_time_bars | 33.9476 |
| exposure | 0.4700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
