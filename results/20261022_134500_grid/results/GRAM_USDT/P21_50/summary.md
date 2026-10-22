# EMA Hourly Continuation — GRAM/USDT P21_50

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.3391 |
| net_win_rate | 0.4144 |
| gross_profit_factor | 0.8147 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -10.2721 |
| sortino_ratio | -4.7165 |
| max_drawdown | 0.9975 |
| cagr | -0.9073 |
| net_avg_win | 11.8220 |
| net_avg_loss | -24.6625 |
| avg_hold_time_bars | 4.1187 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
