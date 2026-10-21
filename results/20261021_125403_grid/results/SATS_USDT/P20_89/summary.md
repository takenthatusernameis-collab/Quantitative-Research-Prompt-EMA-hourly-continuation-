# EMA Hourly Continuation — SATS/USDT P20_89

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7413 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9117 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -2.2683 |
| sortino_ratio | -0.7079 |
| max_drawdown | 0.5969 |
| cagr | -0.2789 |
| net_avg_win | 70.5889 |
| net_avg_loss | -84.8108 |
| avg_hold_time_bars | 17.0207 |
| exposure | 0.3728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
