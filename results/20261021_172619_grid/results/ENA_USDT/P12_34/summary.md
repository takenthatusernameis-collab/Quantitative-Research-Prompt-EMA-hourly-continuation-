# EMA Hourly Continuation — ENA/USDT P12_34

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.8236 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.2398 |
| sortino_ratio | -0.4187 |
| max_drawdown | 0.4561 |
| cagr | -0.1776 |
| net_avg_win | 64.2463 |
| net_avg_loss | -81.1693 |
| avg_hold_time_bars | 7.0597 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
