# EMA Hourly Continuation — CTC/USDT P12_50

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.7358 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.3895 |
| sortino_ratio | -0.9000 |
| max_drawdown | 0.6713 |
| cagr | -0.3399 |
| net_avg_win | 51.8227 |
| net_avg_loss | -71.6677 |
| avg_hold_time_bars | 10.8377 |
| exposure | 0.3399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
