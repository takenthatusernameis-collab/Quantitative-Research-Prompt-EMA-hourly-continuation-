# EMA Hourly Continuation — CRV/USDT P20_89

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6619 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9974 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.7705 |
| sortino_ratio | -1.4488 |
| max_drawdown | 0.8304 |
| cagr | -0.4962 |
| net_avg_win | 44.6645 |
| net_avg_loss | -64.0932 |
| avg_hold_time_bars | 10.3708 |
| exposure | 0.3484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
