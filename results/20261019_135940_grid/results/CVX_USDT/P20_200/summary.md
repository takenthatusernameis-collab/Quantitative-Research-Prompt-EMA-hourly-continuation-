# EMA Hourly Continuation — CVX/USDT P20_200

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7772 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.3203 |
| sortino_ratio | -0.3208 |
| max_drawdown | 0.3325 |
| cagr | -0.1404 |
| net_avg_win | 76.0242 |
| net_avg_loss | -95.8355 |
| avg_hold_time_bars | 52.4266 |
| exposure | 0.6982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
