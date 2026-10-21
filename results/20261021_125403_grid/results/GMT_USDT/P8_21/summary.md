# EMA Hourly Continuation — GMT/USDT P8_21

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.4184 |
| sortino_ratio | -0.8037 |
| max_drawdown | 0.6193 |
| cagr | -0.3071 |
| net_avg_win | 45.7936 |
| net_avg_loss | -68.0842 |
| avg_hold_time_bars | 5.7794 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
