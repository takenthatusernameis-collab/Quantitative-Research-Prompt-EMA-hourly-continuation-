# EMA Hourly Continuation — XNO/USDT P12_21

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.4037 |
| gross_profit_factor | 0.7305 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -4.4169 |
| sortino_ratio | -1.2234 |
| max_drawdown | 0.7593 |
| cagr | -0.4329 |
| net_avg_win | 52.5488 |
| net_avg_loss | -69.1734 |
| avg_hold_time_bars | 4.7361 |
| exposure | 0.0816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
