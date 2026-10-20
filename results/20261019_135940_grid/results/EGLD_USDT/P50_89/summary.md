# EMA Hourly Continuation — EGLD/USDT P50_89

**Symbol:** EGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.4392 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -5.7738 |
| sortino_ratio | -2.0776 |
| max_drawdown | 0.9276 |
| cagr | -0.6430 |
| net_avg_win | 23.9835 |
| net_avg_loss | -46.8469 |
| avg_hold_time_bars | 4.7370 |
| exposure | 0.1408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
