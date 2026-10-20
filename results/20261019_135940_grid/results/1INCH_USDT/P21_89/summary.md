# EMA Hourly Continuation — 1INCH/USDT P21_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.5427 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -5.6717 |
| sortino_ratio | -2.1652 |
| max_drawdown | 0.9298 |
| cagr | -0.6478 |
| net_avg_win | 33.2488 |
| net_avg_loss | -50.3177 |
| avg_hold_time_bars | 12.1662 |
| exposure | 0.4059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
