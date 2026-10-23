# EMA Hourly Continuation — ZPAY/USDT P50_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.3841 |
| net_win_rate | 0.3472 |
| gross_profit_factor | 0.5407 |
| gross_win_rate | 0.3488 |
| sharpe_ratio | -6.8877 |
| sortino_ratio | -2.4092 |
| max_drawdown | 0.9448 |
| cagr | -0.6787 |
| net_avg_win | 27.0954 |
| net_avg_loss | -37.5225 |
| avg_hold_time_bars | 10.7072 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
