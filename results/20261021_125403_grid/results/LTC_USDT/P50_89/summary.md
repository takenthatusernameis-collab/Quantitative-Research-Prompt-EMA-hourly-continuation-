# EMA Hourly Continuation — LTC/USDT P50_89

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.5608 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8328 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.6917 |
| sortino_ratio | -0.6582 |
| max_drawdown | 0.5686 |
| cagr | -0.2608 |
| net_avg_win | 49.5750 |
| net_avg_loss | -78.6385 |
| avg_hold_time_bars | 8.2749 |
| exposure | 0.1095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
