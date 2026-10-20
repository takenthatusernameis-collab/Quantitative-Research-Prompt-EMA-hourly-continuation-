# EMA Hourly Continuation — NYM/USDT P34_100

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.2535 |
| net_win_rate | 0.3351 |
| gross_profit_factor | 0.5699 |
| gross_win_rate | 0.3704 |
| sharpe_ratio | -9.2766 |
| sortino_ratio | -3.1348 |
| max_drawdown | 0.9858 |
| cagr | -0.8138 |
| net_avg_win | 17.6059 |
| net_avg_loss | -35.0087 |
| avg_hold_time_bars | 11.2099 |
| exposure | 0.2889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
