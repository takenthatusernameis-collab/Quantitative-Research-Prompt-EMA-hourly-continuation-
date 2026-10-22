# EMA Hourly Continuation — 1INCH/USDT P8_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -3.3591 |
| sortino_ratio | -0.8435 |
| max_drawdown | 0.6524 |
| cagr | -0.3351 |
| net_avg_win | 57.3280 |
| net_avg_loss | -79.0091 |
| avg_hold_time_bars | 56.8536 |
| exposure | 0.8295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
