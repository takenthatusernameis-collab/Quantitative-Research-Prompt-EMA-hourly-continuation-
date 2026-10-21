# EMA Hourly Continuation — LISTA/USDT P12_50

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.1079 |
| sortino_ratio | -1.1355 |
| max_drawdown | 0.7315 |
| cagr | -0.4070 |
| net_avg_win | 57.6836 |
| net_avg_loss | -70.7843 |
| avg_hold_time_bars | 11.4520 |
| exposure | 0.3444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
