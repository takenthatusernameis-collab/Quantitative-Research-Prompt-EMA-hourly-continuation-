# EMA Hourly Continuation — EDU/USDT P21_26

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8185 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -3.0614 |
| sortino_ratio | -0.7626 |
| max_drawdown | 0.5887 |
| cagr | -0.2968 |
| net_avg_win | 52.3750 |
| net_avg_loss | -79.3188 |
| avg_hold_time_bars | 4.3115 |
| exposure | 0.0595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
