# EMA Hourly Continuation — XNO/USDT P144_200

**Symbol:** XNO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.6162 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -2.5076 |
| sortino_ratio | -0.5596 |
| max_drawdown | 0.4759 |
| cagr | -0.2268 |
| net_avg_win | 69.4634 |
| net_avg_loss | -91.8494 |
| avg_hold_time_bars | 6.3347 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
