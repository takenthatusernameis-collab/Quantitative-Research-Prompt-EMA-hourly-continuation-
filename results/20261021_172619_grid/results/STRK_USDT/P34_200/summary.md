# EMA Hourly Continuation — STRK/USDT P34_200

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8228 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -0.9309 |
| sortino_ratio | -0.2228 |
| max_drawdown | 0.2770 |
| cagr | -0.0990 |
| net_avg_win | 76.9298 |
| net_avg_loss | -92.1742 |
| avg_hold_time_bars | 37.5857 |
| exposure | 0.4784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
