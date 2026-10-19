# EMA Hourly Continuation — AR/USDT P12_55

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.5718 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -5.4722 |
| sortino_ratio | -2.3923 |
| max_drawdown | 0.9472 |
| cagr | -0.6859 |
| net_avg_win | 28.1153 |
| net_avg_loss | -42.3763 |
| avg_hold_time_bars | 9.4175 |
| exposure | 0.4152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
