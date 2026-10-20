# EMA Hourly Continuation — ENJ/USDT P20_34

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1131 |
| net_profit_factor | 0.3629 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.8162 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -10.1728 |
| sortino_ratio | -4.8726 |
| max_drawdown | 0.9979 |
| cagr | -0.9135 |
| net_avg_win | 11.7919 |
| net_avg_loss | -24.1329 |
| avg_hold_time_bars | 2.5650 |
| exposure | 0.1319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
