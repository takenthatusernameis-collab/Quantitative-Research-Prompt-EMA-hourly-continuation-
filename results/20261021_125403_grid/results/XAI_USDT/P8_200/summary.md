# EMA Hourly Continuation — XAI/USDT P8_200

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9953 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1335 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | 0.0259 |
| sortino_ratio | 0.0060 |
| max_drawdown | 0.1814 |
| cagr | -0.0025 |
| net_avg_win | 96.5419 |
| net_avg_loss | -110.7375 |
| avg_hold_time_bars | 71.4086 |
| exposure | 0.8342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
