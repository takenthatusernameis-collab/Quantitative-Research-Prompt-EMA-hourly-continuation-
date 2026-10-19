# EMA Hourly Continuation — RAY/USDT P12_20

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1458 |
| net_profit_factor | 0.4080 |
| net_win_rate | 0.4026 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -12.3554 |
| sortino_ratio | -6.6962 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 11.7393 |
| net_avg_loss | -19.3904 |
| avg_hold_time_bars | 2.2586 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
