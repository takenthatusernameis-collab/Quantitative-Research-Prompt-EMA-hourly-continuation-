# EMA Hourly Continuation — API3/USDT P100_144

**Symbol:** API3/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0691 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -3.9542 |
| sortino_ratio | -1.2793 |
| max_drawdown | 0.7910 |
| cagr | -0.4615 |
| net_avg_win | 45.7071 |
| net_avg_loss | -75.3486 |
| avg_hold_time_bars | 3.9141 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
