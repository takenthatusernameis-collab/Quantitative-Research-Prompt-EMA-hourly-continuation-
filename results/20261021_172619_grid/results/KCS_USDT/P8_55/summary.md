# EMA Hourly Continuation — KCS/USDT P8_55

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.4867 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8074 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -5.4562 |
| sortino_ratio | -1.9016 |
| max_drawdown | 0.8942 |
| cagr | -0.5885 |
| net_avg_win | 32.4181 |
| net_avg_loss | -52.5254 |
| avg_hold_time_bars | 18.1199 |
| exposure | 0.4876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
