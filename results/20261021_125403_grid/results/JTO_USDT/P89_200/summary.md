# EMA Hourly Continuation — JTO/USDT P89_200

**Symbol:** JTO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8137 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -2.1130 |
| sortino_ratio | -0.5169 |
| max_drawdown | 0.4733 |
| cagr | -0.2122 |
| net_avg_win | 69.8319 |
| net_avg_loss | -84.5331 |
| avg_hold_time_bars | 13.0067 |
| exposure | 0.1762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
