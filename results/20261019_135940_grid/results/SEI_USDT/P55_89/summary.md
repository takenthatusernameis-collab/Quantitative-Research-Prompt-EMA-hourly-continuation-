# EMA Hourly Continuation — SEI/USDT P55_89

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8202 |
| gross_win_rate | 0.4360 |
| sharpe_ratio | -6.4090 |
| sortino_ratio | -2.2759 |
| max_drawdown | 0.9413 |
| cagr | -0.6756 |
| net_avg_win | 34.0929 |
| net_avg_loss | -51.7487 |
| avg_hold_time_bars | 4.2780 |
| exposure | 0.1231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
