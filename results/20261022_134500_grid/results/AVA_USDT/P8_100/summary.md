# EMA Hourly Continuation — AVA/USDT P8_100

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -3.8235 |
| sortino_ratio | -1.4003 |
| max_drawdown | 0.8301 |
| cagr | -0.4960 |
| net_avg_win | 35.2935 |
| net_avg_loss | -55.5671 |
| avg_hold_time_bars | 20.0450 |
| exposure | 0.6278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
