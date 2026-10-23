# EMA Hourly Continuation — ID/USDT P20_100

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.6364 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.2544 |
| sortino_ratio | -1.1281 |
| max_drawdown | 0.7502 |
| cagr | -0.4143 |
| net_avg_win | 44.6998 |
| net_avg_loss | -64.2545 |
| avg_hold_time_bars | 16.4135 |
| exposure | 0.4509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
