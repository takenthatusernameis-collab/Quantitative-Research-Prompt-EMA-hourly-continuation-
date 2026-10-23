# EMA Hourly Continuation — ELON/USDT P26_55

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.3618 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7033 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -8.6095 |
| sortino_ratio | -3.5828 |
| max_drawdown | 0.9876 |
| cagr | -0.8258 |
| net_avg_win | 15.9504 |
| net_avg_loss | -30.7641 |
| avg_hold_time_bars | 4.6124 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
