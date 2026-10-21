# EMA Hourly Continuation — SEI/USDT P144_200

**Symbol:** SEI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.6590 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8558 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -1.5953 |
| sortino_ratio | -0.2940 |
| max_drawdown | 0.2990 |
| cagr | -0.1260 |
| net_avg_win | 71.0930 |
| net_avg_loss | -94.5502 |
| avg_hold_time_bars | 8.1317 |
| exposure | 0.0617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
