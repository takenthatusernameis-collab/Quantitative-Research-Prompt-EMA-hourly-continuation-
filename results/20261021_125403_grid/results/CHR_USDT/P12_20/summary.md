# EMA Hourly Continuation — CHR/USDT P12_20

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0328 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.3435 |
| sortino_ratio | -0.7057 |
| max_drawdown | 0.5977 |
| cagr | -0.2762 |
| net_avg_win | 67.9711 |
| net_avg_loss | -92.8904 |
| avg_hold_time_bars | 5.1451 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
