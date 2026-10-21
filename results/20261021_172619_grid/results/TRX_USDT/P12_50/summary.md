# EMA Hourly Continuation — TRX/USDT P12_50

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5032 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 1.0051 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -5.5390 |
| sortino_ratio | -1.9032 |
| max_drawdown | 0.8955 |
| cagr | -0.5839 |
| net_avg_win | 33.2439 |
| net_avg_loss | -62.3811 |
| avg_hold_time_bars | 11.4642 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
