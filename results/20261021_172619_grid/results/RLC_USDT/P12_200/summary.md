# EMA Hourly Continuation — RLC/USDT P12_200

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8796 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0497 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.6009 |
| sortino_ratio | -0.1432 |
| max_drawdown | 0.3228 |
| cagr | -0.0661 |
| net_avg_win | 81.1774 |
| net_avg_loss | -98.5341 |
| avg_hold_time_bars | 61.6909 |
| exposure | 0.7711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
