# EMA Hourly Continuation — WIF/USDT P34_144

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.8222 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -1.1168 |
| sortino_ratio | -0.3100 |
| max_drawdown | 0.3955 |
| cagr | -0.1351 |
| net_avg_win | 75.5536 |
| net_avg_loss | -90.4417 |
| avg_hold_time_bars | 19.4377 |
| exposure | 0.3331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
