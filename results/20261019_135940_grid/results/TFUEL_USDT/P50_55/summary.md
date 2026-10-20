# EMA Hourly Continuation — TFUEL/USDT P50_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.1995 |
| net_win_rate | 0.3045 |
| gross_profit_factor | 0.6026 |
| gross_win_rate | 0.3743 |
| sharpe_ratio | -14.4616 |
| sortino_ratio | -6.4657 |
| max_drawdown | 0.9999 |
| cagr | -0.9709 |
| net_avg_win | 9.0597 |
| net_avg_loss | -19.8887 |
| avg_hold_time_bars | 2.2104 |
| exposure | 0.0903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
