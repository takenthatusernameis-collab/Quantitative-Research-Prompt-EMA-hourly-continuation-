# EMA Hourly Continuation — ENA/USDT P21_100

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0294 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.8663 |
| sortino_ratio | -0.6677 |
| max_drawdown | 0.5716 |
| cagr | -0.2715 |
| net_avg_win | 59.2618 |
| net_avg_loss | -79.5072 |
| avg_hold_time_bars | 13.8135 |
| exposure | 0.4006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
