# EMA Hourly Continuation — FLR/USDT P8_55

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1282 |
| net_profit_factor | 0.4955 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8987 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -8.6425 |
| sortino_ratio | -4.3151 |
| max_drawdown | 0.9959 |
| cagr | -0.8879 |
| net_avg_win | 16.9505 |
| net_avg_loss | -27.9991 |
| avg_hold_time_bars | 7.8947 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
