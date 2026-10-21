# EMA Hourly Continuation — CRO/USDT P12_50

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6067 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -3.6760 |
| sortino_ratio | -1.3386 |
| max_drawdown | 0.7929 |
| cagr | -0.4591 |
| net_avg_win | 38.9936 |
| net_avg_loss | -59.3175 |
| avg_hold_time_bars | 10.6636 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
