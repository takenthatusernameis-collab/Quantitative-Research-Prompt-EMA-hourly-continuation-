# EMA Hourly Continuation — ZIL/USDT P20_21

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1266 |
| net_profit_factor | 0.1181 |
| net_win_rate | 0.2615 |
| gross_profit_factor | 0.6087 |
| gross_win_rate | 0.3633 |
| sharpe_ratio | -19.6299 |
| sortino_ratio | -10.9109 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 4.0441 |
| net_avg_loss | -12.1268 |
| avg_hold_time_bars | 1.6912 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
