# EMA Hourly Continuation — KSM/USDT P12_21

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5862 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -3.7268 |
| sortino_ratio | -1.0859 |
| max_drawdown | 0.7190 |
| cagr | -0.3918 |
| net_avg_win | 53.1702 |
| net_avg_loss | -77.2814 |
| avg_hold_time_bars | 4.5908 |
| exposure | 0.0862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
