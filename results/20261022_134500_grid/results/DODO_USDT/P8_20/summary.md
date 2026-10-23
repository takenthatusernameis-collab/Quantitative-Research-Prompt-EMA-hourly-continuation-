# EMA Hourly Continuation — DODO/USDT P8_20

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1712 |
| net_profit_factor | 0.3686 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -11.9033 |
| sortino_ratio | -6.9287 |
| max_drawdown | 0.9998 |
| cagr | -0.9683 |
| net_avg_win | 8.1409 |
| net_avg_loss | -15.9150 |
| avg_hold_time_bars | 3.2827 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
