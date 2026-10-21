# EMA Hourly Continuation — KCS/USDT P8_12

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.3194 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.6500 |
| gross_win_rate | 0.4057 |
| sharpe_ratio | -5.2885 |
| sortino_ratio | -1.2932 |
| max_drawdown | 0.7884 |
| cagr | -0.4544 |
| net_avg_win | 32.7501 |
| net_avg_loss | -67.9525 |
| avg_hold_time_bars | 6.8683 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
