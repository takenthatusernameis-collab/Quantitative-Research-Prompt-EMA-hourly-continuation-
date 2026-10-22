# EMA Hourly Continuation — CETUS/USDT P8_89

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.8946 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0761 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.7970 |
| sortino_ratio | -0.2593 |
| max_drawdown | 0.3269 |
| cagr | -0.1175 |
| net_avg_win | 85.9612 |
| net_avg_loss | -103.4524 |
| avg_hold_time_bars | 27.6621 |
| exposure | 0.6447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
