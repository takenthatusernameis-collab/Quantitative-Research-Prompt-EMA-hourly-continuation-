# EMA Hourly Continuation — GRAM/USDT P8_12

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1854 |
| net_profit_factor | 0.2010 |
| net_win_rate | 0.3150 |
| gross_profit_factor | 0.7159 |
| gross_win_rate | 0.3851 |
| sharpe_ratio | -21.9127 |
| sortino_ratio | -14.2544 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 4.3064 |
| net_avg_loss | -9.8543 |
| avg_hold_time_bars | 1.6996 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
