# EMA Hourly Continuation — TURBO/USDT P8_21

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1401 |
| net_profit_factor | 0.4629 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7773 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -11.6063 |
| sortino_ratio | -6.6850 |
| max_drawdown | 0.9991 |
| cagr | -0.9651 |
| net_avg_win | 14.9256 |
| net_avg_loss | -22.5766 |
| avg_hold_time_bars | 3.0314 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
