# EMA Hourly Continuation — DIA/USDT P26_200

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.9740 |
| net_win_rate | 0.5457 |
| gross_profit_factor | 1.1859 |
| gross_win_rate | 0.5457 |
| sharpe_ratio | -0.0813 |
| sortino_ratio | -0.0209 |
| max_drawdown | 0.2696 |
| cagr | -0.0152 |
| net_avg_win | 82.1196 |
| net_avg_loss | -101.2899 |
| avg_hold_time_bars | 39.8139 |
| exposure | 0.5711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
