# EMA Hourly Continuation — GMT/USDT P8_144

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.9924 |
| net_win_rate | 0.5390 |
| gross_profit_factor | 1.1630 |
| gross_win_rate | 0.5390 |
| sharpe_ratio | 0.0150 |
| sortino_ratio | 0.0037 |
| max_drawdown | 0.1883 |
| cagr | -0.0042 |
| net_avg_win | 86.8398 |
| net_avg_loss | -102.3028 |
| avg_hold_time_bars | 58.9424 |
| exposure | 0.7904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
