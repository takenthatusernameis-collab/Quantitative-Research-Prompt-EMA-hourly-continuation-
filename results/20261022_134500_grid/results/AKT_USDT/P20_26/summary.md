# EMA Hourly Continuation — AKT/USDT P20_26

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.3410 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -12.6132 |
| sortino_ratio | -6.0634 |
| max_drawdown | 0.9997 |
| cagr | -0.9604 |
| net_avg_win | 11.7291 |
| net_avg_loss | -22.0487 |
| avg_hold_time_bars | 1.9787 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
