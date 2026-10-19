# EMA Hourly Continuation — ZK/USDT P12_55

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.7052 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 1.0488 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -4.6521 |
| sortino_ratio | -2.1062 |
| max_drawdown | 0.9079 |
| cagr | -0.6306 |
| net_avg_win | 46.8554 |
| net_avg_loss | -62.0018 |
| avg_hold_time_bars | 8.4094 |
| exposure | 0.3915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
