# EMA Hourly Continuation — DBR/USDT P12_200

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.4588 |
| net_win_rate | 0.4142 |
| gross_profit_factor | 0.7108 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -4.7146 |
| sortino_ratio | -1.3464 |
| max_drawdown | 0.7515 |
| cagr | -0.4895 |
| net_avg_win | 44.8517 |
| net_avg_loss | -69.1183 |
| avg_hold_time_bars | 35.3195 |
| exposure | 0.6789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
