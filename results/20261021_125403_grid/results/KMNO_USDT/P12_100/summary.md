# EMA Hourly Continuation — KMNO/USDT P12_100

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.7928 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.4358 |
| sortino_ratio | -0.4165 |
| max_drawdown | 0.4018 |
| cagr | -0.1762 |
| net_avg_win | 72.4499 |
| net_avg_loss | -89.1705 |
| avg_hold_time_bars | 30.6904 |
| exposure | 0.5767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
