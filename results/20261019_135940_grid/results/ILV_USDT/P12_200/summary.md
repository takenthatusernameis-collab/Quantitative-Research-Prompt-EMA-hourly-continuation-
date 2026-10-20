# EMA Hourly Continuation — ILV/USDT P12_200

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8767 |
| net_win_rate | 0.5366 |
| gross_profit_factor | 1.1835 |
| gross_win_rate | 0.5436 |
| sharpe_ratio | -0.7276 |
| sortino_ratio | -0.1755 |
| max_drawdown | 0.3259 |
| cagr | -0.0814 |
| net_avg_win | 88.7080 |
| net_avg_loss | -117.1549 |
| avg_hold_time_bars | 60.4425 |
| exposure | 0.7885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
