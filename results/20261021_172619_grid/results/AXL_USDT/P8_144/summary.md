# EMA Hourly Continuation — AXL/USDT P8_144

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -1.9222 |
| sortino_ratio | -0.5923 |
| max_drawdown | 0.5344 |
| cagr | -0.2401 |
| net_avg_win | 77.9658 |
| net_avg_loss | -89.8971 |
| avg_hold_time_bars | 32.9237 |
| exposure | 0.7032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
