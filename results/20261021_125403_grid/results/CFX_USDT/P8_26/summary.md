# EMA Hourly Continuation — CFX/USDT P8_26

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.7853 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0578 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.9869 |
| sortino_ratio | -0.7121 |
| max_drawdown | 0.5766 |
| cagr | -0.2785 |
| net_avg_win | 64.3693 |
| net_avg_loss | -86.3055 |
| avg_hold_time_bars | 7.7758 |
| exposure | 0.2191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
