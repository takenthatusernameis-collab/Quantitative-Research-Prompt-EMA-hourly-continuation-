# EMA Hourly Continuation — KAVA/USDT P8_100

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.6011 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -5.2974 |
| sortino_ratio | -1.9899 |
| max_drawdown | 0.9205 |
| cagr | -0.6252 |
| net_avg_win | 41.4104 |
| net_avg_loss | -59.2737 |
| avg_hold_time_bars | 20.8611 |
| exposure | 0.6827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
