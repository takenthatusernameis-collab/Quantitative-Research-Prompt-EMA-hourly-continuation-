# EMA Hourly Continuation — AVAX/USDT P8_12

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1827 |
| net_profit_factor | 0.1930 |
| net_win_rate | 0.3410 |
| gross_profit_factor | 0.6862 |
| gross_win_rate | 0.3996 |
| sharpe_ratio | -19.6039 |
| sortino_ratio | -12.2887 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 3.8383 |
| net_avg_loss | -10.2917 |
| avg_hold_time_bars | 1.6650 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
