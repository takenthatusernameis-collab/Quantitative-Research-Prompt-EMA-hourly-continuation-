# EMA Hourly Continuation — CHR/USDT P8_144

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8344 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.0160 |
| sortino_ratio | -0.2685 |
| max_drawdown | 0.3436 |
| cagr | -0.1182 |
| net_avg_win | 80.5996 |
| net_avg_loss | -94.9220 |
| avg_hold_time_bars | 50.0087 |
| exposure | 0.7762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
