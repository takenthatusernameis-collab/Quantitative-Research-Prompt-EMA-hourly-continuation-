# EMA Hourly Continuation — ZIL/USDT P21_144

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6711 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 1.0284 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.7150 |
| sortino_ratio | -0.8416 |
| max_drawdown | 0.6663 |
| cagr | -0.3331 |
| net_avg_win | 53.8398 |
| net_avg_loss | -79.5658 |
| avg_hold_time_bars | 24.5226 |
| exposure | 0.5417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
