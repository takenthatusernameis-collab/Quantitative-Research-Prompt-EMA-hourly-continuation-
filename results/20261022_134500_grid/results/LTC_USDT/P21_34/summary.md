# EMA Hourly Continuation — LTC/USDT P21_34

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.2096 |
| net_win_rate | 0.3707 |
| gross_profit_factor | 0.8352 |
| gross_win_rate | 0.4312 |
| sharpe_ratio | -13.8657 |
| sortino_ratio | -6.8071 |
| max_drawdown | 0.9999 |
| cagr | -0.9742 |
| net_avg_win | 6.2695 |
| net_avg_loss | -17.6197 |
| avg_hold_time_bars | 2.2112 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
