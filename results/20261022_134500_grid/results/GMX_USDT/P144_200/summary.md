# EMA Hourly Continuation — GMX/USDT P144_200

**Symbol:** GMX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.5851 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -3.6374 |
| sortino_ratio | -1.0305 |
| max_drawdown | 0.7194 |
| cagr | -0.3890 |
| net_avg_win | 51.8768 |
| net_avg_loss | -84.2894 |
| avg_hold_time_bars | 6.0354 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
