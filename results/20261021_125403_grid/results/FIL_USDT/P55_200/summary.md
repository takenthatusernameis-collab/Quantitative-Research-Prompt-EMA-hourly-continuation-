# EMA Hourly Continuation — FIL/USDT P55_200

**Symbol:** FIL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7774 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.1842 |
| sortino_ratio | -0.2684 |
| max_drawdown | 0.3212 |
| cagr | -0.1164 |
| net_avg_win | 75.2570 |
| net_avg_loss | -94.5198 |
| avg_hold_time_bars | 30.8167 |
| exposure | 0.3516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
