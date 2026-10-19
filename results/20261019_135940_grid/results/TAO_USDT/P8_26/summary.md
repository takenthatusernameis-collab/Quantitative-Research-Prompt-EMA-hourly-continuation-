# EMA Hourly Continuation — TAO/USDT P8_26

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1573 |
| net_profit_factor | 0.5213 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -9.1977 |
| sortino_ratio | -5.1240 |
| max_drawdown | 0.9984 |
| cagr | -0.9210 |
| net_avg_win | 15.3562 |
| net_avg_loss | -24.1100 |
| avg_hold_time_bars | 3.6020 |
| exposure | 0.2575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
