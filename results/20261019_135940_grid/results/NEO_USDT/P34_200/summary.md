# EMA Hourly Continuation — NEO/USDT P34_200

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -3.1659 |
| sortino_ratio | -0.8787 |
| max_drawdown | 0.6564 |
| cagr | -0.3442 |
| net_avg_win | 49.9776 |
| net_avg_loss | -74.6681 |
| avg_hold_time_bars | 28.2366 |
| exposure | 0.5044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
