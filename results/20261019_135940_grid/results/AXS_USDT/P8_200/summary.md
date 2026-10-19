# EMA Hourly Continuation — AXS/USDT P8_200

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -1.9963 |
| sortino_ratio | -0.5104 |
| max_drawdown | 0.5228 |
| cagr | -0.2252 |
| net_avg_win | 69.7206 |
| net_avg_loss | -99.6879 |
| avg_hold_time_bars | 51.4812 |
| exposure | 0.8037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
