# EMA Hourly Continuation — GMT/USDT P12_21

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.2211 |
| net_win_rate | 0.4005 |
| gross_profit_factor | 0.6792 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -13.7807 |
| sortino_ratio | -7.6814 |
| max_drawdown | 1.0000 |
| cagr | -0.9812 |
| net_avg_win | 4.6690 |
| net_avg_loss | -14.1080 |
| avg_hold_time_bars | 2.2516 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
