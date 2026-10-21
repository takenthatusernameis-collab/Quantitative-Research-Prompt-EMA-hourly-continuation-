# EMA Hourly Continuation — ATH/USDT P34_89

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.8578 |
| net_win_rate | 0.5215 |
| gross_profit_factor | 1.0687 |
| gross_win_rate | 0.5215 |
| sharpe_ratio | -0.8892 |
| sortino_ratio | -0.2625 |
| max_drawdown | 0.2804 |
| cagr | -0.1164 |
| net_avg_win | 74.0302 |
| net_avg_loss | -94.0618 |
| avg_hold_time_bars | 10.2481 |
| exposure | 0.1962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
