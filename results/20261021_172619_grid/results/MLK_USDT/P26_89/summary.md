# EMA Hourly Continuation — MLK/USDT P26_89

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.4588 |
| net_win_rate | 0.3711 |
| gross_profit_factor | 0.6444 |
| gross_win_rate | 0.3756 |
| sharpe_ratio | -5.3950 |
| sortino_ratio | -1.6146 |
| max_drawdown | 0.8534 |
| cagr | -0.5294 |
| net_avg_win | 43.1801 |
| net_avg_loss | -55.5366 |
| avg_hold_time_bars | 12.6000 |
| exposure | 0.2566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
