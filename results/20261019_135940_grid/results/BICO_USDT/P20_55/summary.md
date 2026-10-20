# EMA Hourly Continuation — BICO/USDT P20_55

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -5.8603 |
| sortino_ratio | -2.4757 |
| max_drawdown | 0.9476 |
| cagr | -0.6904 |
| net_avg_win | 25.0080 |
| net_avg_loss | -39.4772 |
| avg_hold_time_bars | 6.5073 |
| exposure | 0.2647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
