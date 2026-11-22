# EMA Hourly Continuation — AZERO/USDT P144_200

**Symbol:** AZERO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.5011 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -3.5896 |
| sortino_ratio | -0.9149 |
| max_drawdown | 0.6900 |
| cagr | -0.3497 |
| net_avg_win | 46.1841 |
| net_avg_loss | -74.5672 |
| avg_hold_time_bars | 7.9845 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
