# EMA Hourly Continuation — SKY/USDT P50_89

**Symbol:** SKY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7903 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1322 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -1.4170 |
| sortino_ratio | -0.4053 |
| max_drawdown | 0.3634 |
| cagr | -0.1698 |
| net_avg_win | 69.8306 |
| net_avg_loss | -101.4024 |
| avg_hold_time_bars | 7.3312 |
| exposure | 0.1308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
