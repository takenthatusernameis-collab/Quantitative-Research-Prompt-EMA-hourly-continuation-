# EMA Hourly Continuation — XEC/USDT P20_21

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.7082 |
| sortino_ratio | -0.6420 |
| max_drawdown | 0.5573 |
| cagr | -0.2539 |
| net_avg_win | 53.7278 |
| net_avg_loss | -90.0267 |
| avg_hold_time_bars | 5.0882 |
| exposure | 0.0626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
