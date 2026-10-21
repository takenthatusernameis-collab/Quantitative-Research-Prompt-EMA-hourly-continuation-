# EMA Hourly Continuation — IO/USDT P12_21

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1232 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.7559 |
| sortino_ratio | -0.1932 |
| max_drawdown | 0.2765 |
| cagr | -0.0867 |
| net_avg_win | 81.9184 |
| net_avg_loss | -106.5559 |
| avg_hold_time_bars | 4.3435 |
| exposure | 0.0618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
