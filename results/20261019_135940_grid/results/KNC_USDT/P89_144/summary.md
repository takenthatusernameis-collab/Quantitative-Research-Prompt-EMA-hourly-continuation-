# EMA Hourly Continuation — KNC/USDT P89_144

**Symbol:** KNC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5622 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 1.0115 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -4.1237 |
| sortino_ratio | -1.2339 |
| max_drawdown | 0.7932 |
| cagr | -0.4554 |
| net_avg_win | 46.1052 |
| net_avg_loss | -76.0711 |
| avg_hold_time_bars | 6.3289 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
