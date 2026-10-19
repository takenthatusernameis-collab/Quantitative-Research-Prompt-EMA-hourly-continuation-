# EMA Hourly Continuation — SEI/USDT P20_55

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5844 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -5.8712 |
| sortino_ratio | -2.4969 |
| max_drawdown | 0.9565 |
| cagr | -0.7053 |
| net_avg_win | 30.7508 |
| net_avg_loss | -47.2063 |
| avg_hold_time_bars | 5.8351 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
