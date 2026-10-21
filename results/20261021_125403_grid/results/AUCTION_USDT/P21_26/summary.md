# EMA Hourly Continuation — AUCTION/USDT P21_26

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.7548 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -4.5351 |
| sortino_ratio | -1.2073 |
| max_drawdown | 0.7657 |
| cagr | -0.4335 |
| net_avg_win | 46.0822 |
| net_avg_loss | -72.5352 |
| avg_hold_time_bars | 5.4092 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
