# EMA Hourly Continuation — AZERO/USDT P89_200

**Symbol:** AZERO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.1727 |
| sortino_ratio | -0.5710 |
| max_drawdown | 0.5272 |
| cagr | -0.2342 |
| net_avg_win | 59.0182 |
| net_avg_loss | -82.5643 |
| avg_hold_time_bars | 14.6047 |
| exposure | 0.2273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
