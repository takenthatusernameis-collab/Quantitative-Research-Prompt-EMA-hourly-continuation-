# EMA Hourly Continuation — CRV/USDT P21_144

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9600 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -3.6863 |
| sortino_ratio | -1.2135 |
| max_drawdown | 0.7847 |
| cagr | -0.4451 |
| net_avg_win | 56.5502 |
| net_avg_loss | -75.8253 |
| avg_hold_time_bars | 19.5144 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
