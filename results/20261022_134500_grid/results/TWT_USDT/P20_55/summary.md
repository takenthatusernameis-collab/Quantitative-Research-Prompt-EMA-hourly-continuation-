# EMA Hourly Continuation — TWT/USDT P20_55

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.3910 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8142 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -7.6527 |
| sortino_ratio | -3.4065 |
| max_drawdown | 0.9874 |
| cagr | -0.8205 |
| net_avg_win | 13.5369 |
| net_avg_loss | -30.0027 |
| avg_hold_time_bars | 5.3998 |
| exposure | 0.2474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
