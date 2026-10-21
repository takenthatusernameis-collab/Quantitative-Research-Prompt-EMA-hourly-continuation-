# EMA Hourly Continuation — ZEN/USDT P8_12

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6767 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9822 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.0644 |
| sortino_ratio | -0.5149 |
| max_drawdown | 0.4566 |
| cagr | -0.2102 |
| net_avg_win | 62.3884 |
| net_avg_loss | -90.9793 |
| avg_hold_time_bars | 4.6589 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
