# EMA Hourly Continuation — W/USDT P34_100

**Symbol:** W/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7100 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -2.7210 |
| sortino_ratio | -0.9849 |
| max_drawdown | 0.7028 |
| cagr | -0.3695 |
| net_avg_win | 51.5072 |
| net_avg_loss | -73.2217 |
| avg_hold_time_bars | 9.5994 |
| exposure | 0.2832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
