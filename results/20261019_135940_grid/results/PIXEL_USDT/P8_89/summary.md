# EMA Hourly Continuation — PIXEL/USDT P8_89

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.7279 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.7144 |
| sortino_ratio | -0.9653 |
| max_drawdown | 0.7051 |
| cagr | -0.3668 |
| net_avg_win | 58.8448 |
| net_avg_loss | -76.6557 |
| avg_hold_time_bars | 23.6823 |
| exposure | 0.6848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
