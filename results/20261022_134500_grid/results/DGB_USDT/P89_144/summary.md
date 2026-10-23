# EMA Hourly Continuation — DGB/USDT P89_144

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8515 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -6.1561 |
| sortino_ratio | -2.1141 |
| max_drawdown | 0.9272 |
| cagr | -0.6436 |
| net_avg_win | 32.6582 |
| net_avg_loss | -52.5916 |
| avg_hold_time_bars | 4.6280 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
