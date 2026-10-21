# EMA Hourly Continuation — ICP/USDT P26_89

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.9887 |
| sortino_ratio | -0.6321 |
| max_drawdown | 0.5365 |
| cagr | -0.2519 |
| net_avg_win | 67.2114 |
| net_avg_loss | -85.6888 |
| avg_hold_time_bars | 12.6053 |
| exposure | 0.2830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
