# EMA Hourly Continuation — NMR/USDT P50_89

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -6.0605 |
| sortino_ratio | -2.2650 |
| max_drawdown | 0.9414 |
| cagr | -0.6735 |
| net_avg_win | 29.9207 |
| net_avg_loss | -50.3763 |
| avg_hold_time_bars | 4.8962 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
