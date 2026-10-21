# EMA Hourly Continuation — BSV/USDT P21_34

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6241 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.5160 |
| sortino_ratio | -0.6457 |
| max_drawdown | 0.5274 |
| cagr | -0.2544 |
| net_avg_win | 54.8086 |
| net_avg_loss | -86.7178 |
| avg_hold_time_bars | 5.7201 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
