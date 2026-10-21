# EMA Hourly Continuation — BIGTIME/USDT P12_26

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.7250 |
| sortino_ratio | -1.2439 |
| max_drawdown | 0.7664 |
| cagr | -0.4352 |
| net_avg_win | 47.3359 |
| net_avg_loss | -66.4075 |
| avg_hold_time_bars | 5.8836 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
