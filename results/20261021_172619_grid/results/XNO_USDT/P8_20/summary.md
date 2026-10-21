# EMA Hourly Continuation — XNO/USDT P8_20

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -4.4130 |
| sortino_ratio | -1.4922 |
| max_drawdown | 0.8235 |
| cagr | -0.4970 |
| net_avg_win | 50.3339 |
| net_avg_loss | -64.6280 |
| avg_hold_time_bars | 4.9982 |
| exposure | 0.1279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
