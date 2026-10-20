# EMA Hourly Continuation — UMA/USDT P8_26

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1484 |
| net_profit_factor | 0.3707 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7511 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -10.6409 |
| sortino_ratio | -5.7820 |
| max_drawdown | 0.9993 |
| cagr | -0.9431 |
| net_avg_win | 9.3595 |
| net_avg_loss | -18.5727 |
| avg_hold_time_bars | 4.2082 |
| exposure | 0.2839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
