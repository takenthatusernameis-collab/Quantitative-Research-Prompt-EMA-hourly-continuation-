# EMA Hourly Continuation — HTR/USDT P50_89

**Symbol:** HTR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.3875 |
| net_win_rate | 0.3843 |
| gross_profit_factor | 0.6538 |
| gross_win_rate | 0.4052 |
| sharpe_ratio | -8.4799 |
| sortino_ratio | -3.2966 |
| max_drawdown | 0.9858 |
| cagr | -0.8112 |
| net_avg_win | 21.1933 |
| net_avg_loss | -34.1376 |
| avg_hold_time_bars | 4.7098 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
