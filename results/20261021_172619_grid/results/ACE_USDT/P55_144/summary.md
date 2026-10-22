# EMA Hourly Continuation — ACE/USDT P55_144

**Symbol:** ACE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -1.7358 |
| sortino_ratio | -0.4555 |
| max_drawdown | 0.4508 |
| cagr | -0.1897 |
| net_avg_win | 75.1543 |
| net_avg_loss | -93.4253 |
| avg_hold_time_bars | 16.2882 |
| exposure | 0.2506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
