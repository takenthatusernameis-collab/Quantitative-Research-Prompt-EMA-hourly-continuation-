# EMA Hourly Continuation — LTC/USDT P50_200

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.5706 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.7702 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -2.6969 |
| sortino_ratio | -0.6423 |
| max_drawdown | 0.5340 |
| cagr | -0.2565 |
| net_avg_win | 55.8169 |
| net_avg_loss | -78.3795 |
| avg_hold_time_bars | 29.3915 |
| exposure | 0.3754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
