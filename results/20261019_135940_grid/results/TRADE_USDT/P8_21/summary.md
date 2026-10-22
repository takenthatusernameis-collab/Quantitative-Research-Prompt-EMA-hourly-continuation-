# EMA Hourly Continuation — TRADE/USDT P8_21

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1408 |
| net_profit_factor | 0.4755 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4027 |
| sharpe_ratio | -11.9755 |
| sortino_ratio | -6.3312 |
| max_drawdown | 0.9997 |
| cagr | -0.9613 |
| net_avg_win | 16.4509 |
| net_avg_loss | -22.2423 |
| avg_hold_time_bars | 4.0305 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
