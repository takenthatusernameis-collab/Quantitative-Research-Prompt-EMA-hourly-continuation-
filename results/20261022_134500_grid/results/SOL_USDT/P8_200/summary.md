# EMA Hourly Continuation — SOL/USDT P8_200

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7276 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0022 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.5572 |
| sortino_ratio | -0.3903 |
| max_drawdown | 0.4289 |
| cagr | -0.1692 |
| net_avg_win | 62.9424 |
| net_avg_loss | -88.1774 |
| avg_hold_time_bars | 57.6741 |
| exposure | 0.8205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
