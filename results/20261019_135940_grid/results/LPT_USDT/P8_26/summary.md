# EMA Hourly Continuation — LPT/USDT P8_26

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.5222 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -10.2175 |
| sortino_ratio | -5.7547 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 15.5363 |
| net_avg_loss | -23.3938 |
| avg_hold_time_bars | 3.7320 |
| exposure | 0.2709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
