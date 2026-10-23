# EMA Hourly Continuation — DUSK/USDT P8_21

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 1.0543 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -8.8738 |
| sortino_ratio | -5.0166 |
| max_drawdown | 0.9980 |
| cagr | -0.9147 |
| net_avg_win | 16.8871 |
| net_avg_loss | -25.5023 |
| avg_hold_time_bars | 3.2726 |
| exposure | 0.2407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
