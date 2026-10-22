# EMA Hourly Continuation — LTC/USDT P34_89

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.3955 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -7.7968 |
| sortino_ratio | -2.9563 |
| max_drawdown | 0.9772 |
| cagr | -0.7719 |
| net_avg_win | 21.4148 |
| net_avg_loss | -38.3307 |
| avg_hold_time_bars | 7.4562 |
| exposure | 0.2437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
