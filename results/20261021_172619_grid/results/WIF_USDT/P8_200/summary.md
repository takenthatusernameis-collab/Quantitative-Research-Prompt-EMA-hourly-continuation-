# EMA Hourly Continuation — WIF/USDT P8_200

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.8074 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9143 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.0916 |
| sortino_ratio | -0.2581 |
| max_drawdown | 0.2873 |
| cagr | -0.1132 |
| net_avg_win | 82.7130 |
| net_avg_loss | -93.9091 |
| avg_hold_time_bars | 62.6123 |
| exposure | 0.7855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
