# EMA Hourly Continuation — BONK/USDT P12_89

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -3.1472 |
| sortino_ratio | -1.1531 |
| max_drawdown | 0.7774 |
| cagr | -0.4308 |
| net_avg_win | 53.2062 |
| net_avg_loss | -74.6265 |
| avg_hold_time_bars | 17.9536 |
| exposure | 0.5623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
