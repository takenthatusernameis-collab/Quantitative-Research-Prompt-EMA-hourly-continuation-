# EMA Hourly Continuation — HNT/USDT P12_89

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8195 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -5.0454 |
| sortino_ratio | -2.0132 |
| max_drawdown | 0.9165 |
| cagr | -0.6217 |
| net_avg_win | 31.4573 |
| net_avg_loss | -46.1811 |
| avg_hold_time_bars | 13.7737 |
| exposure | 0.5090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
