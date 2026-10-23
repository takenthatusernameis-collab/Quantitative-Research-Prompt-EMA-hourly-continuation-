# EMA Hourly Continuation — ALT/USDT P144_200

**Symbol:** ALT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.5496 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8741 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.4515 |
| sortino_ratio | -0.9510 |
| max_drawdown | 0.7005 |
| cagr | -0.3616 |
| net_avg_win | 47.6838 |
| net_avg_loss | -73.5734 |
| avg_hold_time_bars | 6.6048 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
