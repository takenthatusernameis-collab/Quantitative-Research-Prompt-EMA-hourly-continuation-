# EMA Hourly Continuation — TWT/USDT P100_144

**Symbol:** TWT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.4883 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.7638 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -3.3482 |
| sortino_ratio | -0.7425 |
| max_drawdown | 0.5804 |
| cagr | -0.2898 |
| net_avg_win | 52.9012 |
| net_avg_loss | -83.4576 |
| avg_hold_time_bars | 7.4268 |
| exposure | 0.0807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
