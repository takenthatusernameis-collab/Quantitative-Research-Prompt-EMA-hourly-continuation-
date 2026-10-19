# EMA Hourly Continuation — ETC/USDT P8_12

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1863 |
| net_profit_factor | 0.1574 |
| net_win_rate | 0.2947 |
| gross_profit_factor | 0.7120 |
| gross_win_rate | 0.3994 |
| sharpe_ratio | -21.9852 |
| sortino_ratio | -14.2618 |
| max_drawdown | 1.0000 |
| cagr | -0.9996 |
| net_avg_win | 3.4029 |
| net_avg_loss | -9.0321 |
| avg_hold_time_bars | 1.7466 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
