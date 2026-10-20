# EMA Hourly Continuation — ZIL/USDT P50_89

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4829 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -6.3012 |
| sortino_ratio | -2.3864 |
| max_drawdown | 0.9483 |
| cagr | -0.6890 |
| net_avg_win | 27.2873 |
| net_avg_loss | -46.8251 |
| avg_hold_time_bars | 4.6000 |
| exposure | 0.1495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
