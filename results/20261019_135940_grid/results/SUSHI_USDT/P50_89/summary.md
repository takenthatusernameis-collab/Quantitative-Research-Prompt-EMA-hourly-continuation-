# EMA Hourly Continuation — SUSHI/USDT P50_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4904 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8282 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -6.3909 |
| sortino_ratio | -2.3713 |
| max_drawdown | 0.9504 |
| cagr | -0.6923 |
| net_avg_win | 30.0424 |
| net_avg_loss | -46.6706 |
| avg_hold_time_bars | 4.8734 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
