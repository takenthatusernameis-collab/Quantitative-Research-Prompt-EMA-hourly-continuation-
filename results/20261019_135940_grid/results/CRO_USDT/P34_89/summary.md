# EMA Hourly Continuation — CRO/USDT P34_89

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.3867 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.8459 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -7.5805 |
| sortino_ratio | -2.8377 |
| max_drawdown | 0.9762 |
| cagr | -0.7689 |
| net_avg_win | 20.0215 |
| net_avg_loss | -39.2446 |
| avg_hold_time_bars | 7.8118 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
