# EMA Hourly Continuation — LTC/USDT P21_89

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.4232 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.8103 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -7.3028 |
| sortino_ratio | -2.8100 |
| max_drawdown | 0.9707 |
| cagr | -0.7496 |
| net_avg_win | 22.5022 |
| net_avg_loss | -39.0740 |
| avg_hold_time_bars | 10.4357 |
| exposure | 0.3539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
