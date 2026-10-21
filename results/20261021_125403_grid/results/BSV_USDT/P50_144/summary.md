# EMA Hourly Continuation — BSV/USDT P50_144

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4070 |
| gross_profit_factor | 0.6745 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -3.8922 |
| sortino_ratio | -1.0602 |
| max_drawdown | 0.7081 |
| cagr | -0.3876 |
| net_avg_win | 49.3715 |
| net_avg_loss | -66.0741 |
| avg_hold_time_bars | 18.1078 |
| exposure | 0.3054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
