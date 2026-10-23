# EMA Hourly Continuation — CHR/USDT P12_50

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.5067 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -7.1142 |
| sortino_ratio | -3.2728 |
| max_drawdown | 0.9822 |
| cagr | -0.7929 |
| net_avg_win | 21.6778 |
| net_avg_loss | -32.6096 |
| avg_hold_time_bars | 7.3126 |
| exposure | 0.3557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
