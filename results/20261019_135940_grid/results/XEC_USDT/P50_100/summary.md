# EMA Hourly Continuation — XEC/USDT P50_100

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4058 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.7440 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -6.6271 |
| sortino_ratio | -2.4508 |
| max_drawdown | 0.9527 |
| cagr | -0.6984 |
| net_avg_win | 22.0216 |
| net_avg_loss | -40.7387 |
| avg_hold_time_bars | 6.1163 |
| exposure | 0.1904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
