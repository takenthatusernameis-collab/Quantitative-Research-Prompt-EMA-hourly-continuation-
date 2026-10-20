# EMA Hourly Continuation — BRETT/USDT P8_200

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -0.7766 |
| sortino_ratio | -0.1739 |
| max_drawdown | 0.2569 |
| cagr | -0.0797 |
| net_avg_win | 75.3935 |
| net_avg_loss | -93.5730 |
| avg_hold_time_bars | 76.2222 |
| exposure | 0.8582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
