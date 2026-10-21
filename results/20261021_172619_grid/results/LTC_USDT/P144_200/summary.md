# EMA Hourly Continuation — LTC/USDT P144_200

**Symbol:** LTC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.6581 |
| net_win_rate | 0.5160 |
| gross_profit_factor | 1.0300 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -1.6347 |
| sortino_ratio | -0.3227 |
| max_drawdown | 0.3237 |
| cagr | -0.1361 |
| net_avg_win | 61.0199 |
| net_avg_loss | -98.8389 |
| avg_hold_time_bars | 6.1755 |
| exposure | 0.0528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
