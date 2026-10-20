# EMA Hourly Continuation — AVA/USDT P144_200

**Symbol:** AVA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.4760 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -3.8557 |
| sortino_ratio | -1.0470 |
| max_drawdown | 0.7290 |
| cagr | -0.4021 |
| net_avg_win | 36.8013 |
| net_avg_loss | -72.4586 |
| avg_hold_time_bars | 4.1054 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
