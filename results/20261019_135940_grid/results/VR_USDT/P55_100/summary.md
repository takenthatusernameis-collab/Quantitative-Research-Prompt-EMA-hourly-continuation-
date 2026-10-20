# EMA Hourly Continuation — VR/USDT P55_100

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.3753 |
| net_win_rate | 0.3014 |
| gross_profit_factor | 0.6446 |
| gross_win_rate | 0.3139 |
| sharpe_ratio | -12.1276 |
| sortino_ratio | -4.6711 |
| max_drawdown | 0.9989 |
| cagr | -0.9343 |
| net_avg_win | 27.6580 |
| net_avg_loss | -31.7913 |
| avg_hold_time_bars | 4.5236 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
