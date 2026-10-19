# EMA Hourly Continuation — BSV/USDT P12_50

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1174 |
| net_profit_factor | 0.4247 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7954 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -8.9712 |
| sortino_ratio | -4.3043 |
| max_drawdown | 0.9957 |
| cagr | -0.8837 |
| net_avg_win | 14.6967 |
| net_avg_loss | -25.6726 |
| avg_hold_time_bars | 6.5349 |
| exposure | 0.3487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
