# EMA Hourly Continuation — JST/USDT P8_55

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6087 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0205 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -3.7456 |
| sortino_ratio | -1.3255 |
| max_drawdown | 0.7931 |
| cagr | -0.4594 |
| net_avg_win | 39.8063 |
| net_avg_loss | -64.9714 |
| avg_hold_time_bars | 16.8981 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
