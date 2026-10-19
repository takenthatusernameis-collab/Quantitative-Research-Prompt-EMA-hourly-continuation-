# EMA Hourly Continuation — JUP/USDT P12_20

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1570 |
| net_profit_factor | 0.3490 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8194 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -13.2129 |
| sortino_ratio | -7.4301 |
| max_drawdown | 0.9999 |
| cagr | -0.9782 |
| net_avg_win | 8.3488 |
| net_avg_loss | -16.5509 |
| avg_hold_time_bars | 1.9643 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
