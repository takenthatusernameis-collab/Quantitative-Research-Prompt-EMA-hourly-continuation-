# EMA Hourly Continuation — KSM/USDT P20_89

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.2757 |
| sortino_ratio | -0.7047 |
| max_drawdown | 0.6064 |
| cagr | -0.2772 |
| net_avg_win | 66.8491 |
| net_avg_loss | -85.6620 |
| avg_hold_time_bars | 19.0828 |
| exposure | 0.4085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
