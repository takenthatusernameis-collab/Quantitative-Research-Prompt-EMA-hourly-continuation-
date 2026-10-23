# EMA Hourly Continuation — ELON/USDT P8_34

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1398 |
| net_profit_factor | 0.3873 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.7039 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -9.7082 |
| sortino_ratio | -5.1559 |
| max_drawdown | 0.9981 |
| cagr | -0.9165 |
| net_avg_win | 10.5507 |
| net_avg_loss | -20.3622 |
| avg_hold_time_bars | 5.1631 |
| exposure | 0.3281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
