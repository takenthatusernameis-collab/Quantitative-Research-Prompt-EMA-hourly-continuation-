# EMA Hourly Continuation — RAY/USDT P20_21

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.2056 |
| net_win_rate | 0.3136 |
| gross_profit_factor | 0.7189 |
| gross_win_rate | 0.3831 |
| sharpe_ratio | -16.3422 |
| sortino_ratio | -8.3262 |
| max_drawdown | 1.0000 |
| cagr | -0.9907 |
| net_avg_win | 6.9933 |
| net_avg_loss | -15.5400 |
| avg_hold_time_bars | 1.8280 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
