# EMA Hourly Continuation — SKY/USDT P55_89

**Symbol:** SKY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 1.0229 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -5.5490 |
| sortino_ratio | -2.0378 |
| max_drawdown | 0.8813 |
| cagr | -0.6409 |
| net_avg_win | 34.4638 |
| net_avg_loss | -64.3614 |
| avg_hold_time_bars | 4.3178 |
| exposure | 0.1341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
