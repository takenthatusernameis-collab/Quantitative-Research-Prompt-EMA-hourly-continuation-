# EMA Hourly Continuation — 1INCH/USDT P50_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 862 |
| net_profit_factor | 0.1680 |
| net_win_rate | 0.3109 |
| gross_profit_factor | 0.6077 |
| gross_win_rate | 0.3968 |
| sharpe_ratio | -14.0443 |
| sortino_ratio | -6.1830 |
| max_drawdown | 0.9998 |
| cagr | -0.9671 |
| net_avg_win | 7.5326 |
| net_avg_loss | -20.2304 |
| avg_hold_time_bars | 1.8968 |
| exposure | 0.0743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
