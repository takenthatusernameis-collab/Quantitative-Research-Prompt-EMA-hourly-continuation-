# EMA Hourly Continuation — LSK/USDT P26_200

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7352 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.7804 |
| sortino_ratio | -0.4737 |
| max_drawdown | 0.5050 |
| cagr | -0.2037 |
| net_avg_win | 66.8223 |
| net_avg_loss | -92.4246 |
| avg_hold_time_bars | 34.4123 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
