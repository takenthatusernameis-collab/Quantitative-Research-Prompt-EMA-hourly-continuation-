# EMA Hourly Continuation — APT/USDT P8_21

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1682 |
| net_profit_factor | 0.3064 |
| net_win_rate | 0.4120 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -13.1962 |
| sortino_ratio | -7.6394 |
| max_drawdown | 0.9999 |
| cagr | -0.9800 |
| net_avg_win | 6.3728 |
| net_avg_loss | -14.5762 |
| avg_hold_time_bars | 2.8317 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
