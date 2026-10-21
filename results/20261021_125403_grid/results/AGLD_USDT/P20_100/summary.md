# EMA Hourly Continuation — AGLD/USDT P20_100

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.7289 |
| sortino_ratio | -0.8822 |
| max_drawdown | 0.6959 |
| cagr | -0.3335 |
| net_avg_win | 67.4184 |
| net_avg_loss | -80.6685 |
| avg_hold_time_bars | 18.9462 |
| exposure | 0.4459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
