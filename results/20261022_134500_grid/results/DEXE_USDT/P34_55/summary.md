# EMA Hourly Continuation — DEXE/USDT P34_55

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 865 |
| net_profit_factor | 0.3711 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -8.7435 |
| sortino_ratio | -3.6317 |
| max_drawdown | 0.9903 |
| cagr | -0.8401 |
| net_avg_win | 16.2703 |
| net_avg_loss | -31.1086 |
| avg_hold_time_bars | 5.5688 |
| exposure | 0.2190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
