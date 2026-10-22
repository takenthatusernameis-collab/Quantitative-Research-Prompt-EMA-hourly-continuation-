# EMA Hourly Continuation — WAVES/USDT P34_50

**Symbol:** WAVES/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.4649 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.7374 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -4.2118 |
| sortino_ratio | -1.0115 |
| max_drawdown | 0.6940 |
| cagr | -0.3760 |
| net_avg_win | 51.9781 |
| net_avg_loss | -78.6025 |
| avg_hold_time_bars | 5.9324 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
