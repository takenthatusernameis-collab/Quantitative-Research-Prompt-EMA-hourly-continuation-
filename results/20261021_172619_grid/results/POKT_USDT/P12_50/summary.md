# EMA Hourly Continuation — POKT/USDT P12_50

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -4.3698 |
| sortino_ratio | -1.6125 |
| max_drawdown | 0.8516 |
| cagr | -0.5258 |
| net_avg_win | 50.1203 |
| net_avg_loss | -58.8106 |
| avg_hold_time_bars | 9.4336 |
| exposure | 0.2924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
