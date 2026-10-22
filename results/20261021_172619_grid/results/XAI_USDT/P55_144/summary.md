# EMA Hourly Continuation — XAI/USDT P55_144

**Symbol:** XAI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -2.0970 |
| sortino_ratio | -0.5702 |
| max_drawdown | 0.5431 |
| cagr | -0.2313 |
| net_avg_win | 70.0055 |
| net_avg_loss | -86.6245 |
| avg_hold_time_bars | 17.3836 |
| exposure | 0.2884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
