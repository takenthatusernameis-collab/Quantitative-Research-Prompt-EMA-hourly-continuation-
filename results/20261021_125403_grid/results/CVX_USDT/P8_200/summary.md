# EMA Hourly Continuation — CVX/USDT P8_200

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.9354 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0600 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -0.2689 |
| sortino_ratio | -0.0559 |
| max_drawdown | 0.1534 |
| cagr | -0.0283 |
| net_avg_win | 93.3668 |
| net_avg_loss | -105.6875 |
| avg_hold_time_bars | 89.4524 |
| exposure | 0.8539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
