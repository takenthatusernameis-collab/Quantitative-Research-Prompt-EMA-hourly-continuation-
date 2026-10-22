# EMA Hourly Continuation — DIA/USDT P12_100

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.3793 |
| sortino_ratio | -0.7905 |
| max_drawdown | 0.6365 |
| cagr | -0.3059 |
| net_avg_win | 59.5065 |
| net_avg_loss | -74.1565 |
| avg_hold_time_bars | 21.0146 |
| exposure | 0.5211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
