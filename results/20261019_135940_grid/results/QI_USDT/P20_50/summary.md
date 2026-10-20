# EMA Hourly Continuation — QI/USDT P20_50

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4796 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8696 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -7.2219 |
| sortino_ratio | -3.0916 |
| max_drawdown | 0.9787 |
| cagr | -0.7799 |
| net_avg_win | 21.8816 |
| net_avg_loss | -36.1454 |
| avg_hold_time_bars | 5.1685 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
