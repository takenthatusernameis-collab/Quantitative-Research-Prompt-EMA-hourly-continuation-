# EMA Hourly Continuation — MINA/USDT P144_200

**Symbol:** MINA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.7054 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0037 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.5733 |
| sortino_ratio | -0.3424 |
| max_drawdown | 0.3565 |
| cagr | -0.1459 |
| net_avg_win | 67.4821 |
| net_avg_loss | -98.2062 |
| avg_hold_time_bars | 6.8865 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
