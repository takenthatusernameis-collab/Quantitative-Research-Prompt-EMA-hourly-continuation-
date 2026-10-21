# EMA Hourly Continuation — CRV/USDT P12_100

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8548 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0266 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.0114 |
| sortino_ratio | -0.3040 |
| max_drawdown | 0.3383 |
| cagr | -0.1329 |
| net_avg_win | 79.4232 |
| net_avg_loss | -95.9301 |
| avg_hold_time_bars | 28.6469 |
| exposure | 0.5716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
