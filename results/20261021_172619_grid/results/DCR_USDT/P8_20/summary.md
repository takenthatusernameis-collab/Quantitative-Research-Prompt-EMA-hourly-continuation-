# EMA Hourly Continuation — DCR/USDT P8_20

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5148 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.7868 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -4.8420 |
| sortino_ratio | -1.7678 |
| max_drawdown | 0.8720 |
| cagr | -0.5573 |
| net_avg_win | 31.4738 |
| net_avg_loss | -49.7872 |
| avg_hold_time_bars | 5.7771 |
| exposure | 0.1712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
