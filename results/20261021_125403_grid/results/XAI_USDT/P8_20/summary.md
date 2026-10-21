# EMA Hourly Continuation — XAI/USDT P8_20

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.9286 |
| sortino_ratio | -1.0503 |
| max_drawdown | 0.7118 |
| cagr | -0.3817 |
| net_avg_win | 49.9102 |
| net_avg_loss | -67.8940 |
| avg_hold_time_bars | 5.2083 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
