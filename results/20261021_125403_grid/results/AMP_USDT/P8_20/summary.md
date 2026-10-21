# EMA Hourly Continuation — AMP/USDT P8_20

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4330 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.6425 |
| gross_win_rate | 0.3885 |
| sharpe_ratio | -6.2974 |
| sortino_ratio | -2.1526 |
| max_drawdown | 0.9206 |
| cagr | -0.6313 |
| net_avg_win | 31.4523 |
| net_avg_loss | -46.1472 |
| avg_hold_time_bars | 4.8624 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
