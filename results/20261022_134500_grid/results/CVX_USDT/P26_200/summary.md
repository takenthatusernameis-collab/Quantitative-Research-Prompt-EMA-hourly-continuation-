# EMA Hourly Continuation — CVX/USDT P26_200

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8828 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.8018 |
| sortino_ratio | -0.8163 |
| max_drawdown | 0.6273 |
| cagr | -0.3206 |
| net_avg_win | 58.8060 |
| net_avg_loss | -77.0440 |
| avg_hold_time_bars | 27.1822 |
| exposure | 0.5288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
