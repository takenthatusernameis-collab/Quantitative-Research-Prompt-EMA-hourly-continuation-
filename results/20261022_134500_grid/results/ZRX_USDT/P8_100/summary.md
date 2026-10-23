# EMA Hourly Continuation — ZRX/USDT P8_100

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6597 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9675 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -3.4993 |
| sortino_ratio | -1.2072 |
| max_drawdown | 0.7789 |
| cagr | -0.4415 |
| net_avg_win | 51.1999 |
| net_avg_loss | -71.0177 |
| avg_hold_time_bars | 24.6601 |
| exposure | 0.6826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
