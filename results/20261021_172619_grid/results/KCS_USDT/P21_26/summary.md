# EMA Hourly Continuation — KCS/USDT P21_26

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.3038 |
| net_win_rate | 0.3743 |
| gross_profit_factor | 0.6640 |
| gross_win_rate | 0.3855 |
| sharpe_ratio | -4.6840 |
| sortino_ratio | -0.9158 |
| max_drawdown | 0.6672 |
| cagr | -0.3547 |
| net_avg_win | 43.4541 |
| net_avg_loss | -85.5669 |
| avg_hold_time_bars | 5.7989 |
| exposure | 0.0472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
