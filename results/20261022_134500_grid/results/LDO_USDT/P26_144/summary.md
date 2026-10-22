# EMA Hourly Continuation — LDO/USDT P26_144

**Symbol:** LDO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6170 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -3.5375 |
| sortino_ratio | -1.1142 |
| max_drawdown | 0.7392 |
| cagr | -0.4119 |
| net_avg_win | 52.0252 |
| net_avg_loss | -69.6588 |
| avg_hold_time_bars | 20.3194 |
| exposure | 0.4655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
