# EMA Hourly Continuation — IO/USDT P8_89

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.6371 |
| sortino_ratio | -0.5251 |
| max_drawdown | 0.4813 |
| cagr | -0.2163 |
| net_avg_win | 76.4327 |
| net_avg_loss | -88.5588 |
| avg_hold_time_bars | 26.6176 |
| exposure | 0.6134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
