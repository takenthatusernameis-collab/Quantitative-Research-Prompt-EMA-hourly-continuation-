# EMA Hourly Continuation — GTC/USDT P21_26

**Symbol:** GTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -2.8541 |
| sortino_ratio | -0.7055 |
| max_drawdown | 0.5823 |
| cagr | -0.2758 |
| net_avg_win | 55.8778 |
| net_avg_loss | -84.6625 |
| avg_hold_time_bars | 5.2450 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
