# EMA Hourly Continuation — CKB/USDT P8_144

**Symbol:** CKB/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8485 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -0.9063 |
| sortino_ratio | -0.2365 |
| max_drawdown | 0.2769 |
| cagr | -0.1053 |
| net_avg_win | 81.2976 |
| net_avg_loss | -98.1478 |
| avg_hold_time_bars | 51.6145 |
| exposure | 0.7789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
