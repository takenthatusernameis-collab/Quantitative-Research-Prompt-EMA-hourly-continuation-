# EMA Hourly Continuation — XCH/USDT P20_100

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0777 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -0.9255 |
| sortino_ratio | -0.3048 |
| max_drawdown | 0.3546 |
| cagr | -0.1342 |
| net_avg_win | 71.2247 |
| net_avg_loss | -89.9256 |
| avg_hold_time_bars | 18.7285 |
| exposure | 0.4452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
