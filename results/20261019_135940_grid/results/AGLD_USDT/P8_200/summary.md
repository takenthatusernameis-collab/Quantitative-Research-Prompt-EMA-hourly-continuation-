# EMA Hourly Continuation — AGLD/USDT P8_200

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9461 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.3307 |
| sortino_ratio | -0.6584 |
| max_drawdown | 0.5890 |
| cagr | -0.2651 |
| net_avg_win | 70.3243 |
| net_avg_loss | -88.0893 |
| avg_hold_time_bars | 42.3449 |
| exposure | 0.7723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
