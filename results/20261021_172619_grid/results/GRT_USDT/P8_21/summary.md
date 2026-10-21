# EMA Hourly Continuation — GRT/USDT P8_21

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.8810 |
| sortino_ratio | -0.9680 |
| max_drawdown | 0.6764 |
| cagr | -0.3585 |
| net_avg_win | 60.6027 |
| net_avg_loss | -80.9099 |
| avg_hold_time_bars | 5.5543 |
| exposure | 0.1387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
