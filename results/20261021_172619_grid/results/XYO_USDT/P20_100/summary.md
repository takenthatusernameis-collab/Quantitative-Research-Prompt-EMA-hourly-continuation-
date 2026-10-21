# EMA Hourly Continuation — XYO/USDT P20_100

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6367 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8316 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -3.5103 |
| sortino_ratio | -1.1034 |
| max_drawdown | 0.7333 |
| cagr | -0.3988 |
| net_avg_win | 57.8409 |
| net_avg_loss | -72.6150 |
| avg_hold_time_bars | 17.8053 |
| exposure | 0.3972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
