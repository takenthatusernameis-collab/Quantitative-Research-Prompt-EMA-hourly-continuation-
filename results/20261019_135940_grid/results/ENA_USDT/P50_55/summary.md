# EMA Hourly Continuation — ENA/USDT P50_55

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 746 |
| net_profit_factor | 0.2971 |
| net_win_rate | 0.3794 |
| gross_profit_factor | 0.6890 |
| gross_win_rate | 0.4129 |
| sharpe_ratio | -10.0680 |
| sortino_ratio | -3.9375 |
| max_drawdown | 0.9947 |
| cagr | -0.8754 |
| net_avg_win | 14.8550 |
| net_avg_loss | -30.5624 |
| avg_hold_time_bars | 1.8861 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
