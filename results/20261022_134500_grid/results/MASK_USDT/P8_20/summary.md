# EMA Hourly Continuation — MASK/USDT P8_20

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1592 |
| net_profit_factor | 0.3077 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.8345 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -12.5716 |
| sortino_ratio | -7.0991 |
| max_drawdown | 0.9999 |
| cagr | -0.9739 |
| net_avg_win | 6.6336 |
| net_avg_loss | -15.6654 |
| avg_hold_time_bars | 3.5854 |
| exposure | 0.2595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
