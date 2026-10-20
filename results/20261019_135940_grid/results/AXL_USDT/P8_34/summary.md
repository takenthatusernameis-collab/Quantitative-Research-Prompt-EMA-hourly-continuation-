# EMA Hourly Continuation — AXL/USDT P8_34

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1465 |
| net_profit_factor | 0.5401 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.8748 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -8.9997 |
| sortino_ratio | -4.8146 |
| max_drawdown | 0.9973 |
| cagr | -0.9047 |
| net_avg_win | 18.8292 |
| net_avg_loss | -25.7238 |
| avg_hold_time_bars | 5.4532 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
