# EMA Hourly Continuation — NYM/USDT P12_21

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.3095 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.6552 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -5.6755 |
| sortino_ratio | -1.5696 |
| max_drawdown | 0.8492 |
| cagr | -0.5243 |
| net_avg_win | 25.2555 |
| net_avg_loss | -55.3878 |
| avg_hold_time_bars | 8.7278 |
| exposure | 0.1472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
