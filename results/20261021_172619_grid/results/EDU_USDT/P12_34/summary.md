# EMA Hourly Continuation — EDU/USDT P12_34

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.7553 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.3106 |
| sortino_ratio | -0.8771 |
| max_drawdown | 0.6430 |
| cagr | -0.3323 |
| net_avg_win | 55.8774 |
| net_avg_loss | -74.4016 |
| avg_hold_time_bars | 6.8864 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
