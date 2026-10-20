# EMA Hourly Continuation — DOGS/USDT P8_89

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -3.6747 |
| sortino_ratio | -1.4689 |
| max_drawdown | 0.7909 |
| cagr | -0.5095 |
| net_avg_win | 52.0486 |
| net_avg_loss | -71.6789 |
| avg_hold_time_bars | 16.3711 |
| exposure | 0.6062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
