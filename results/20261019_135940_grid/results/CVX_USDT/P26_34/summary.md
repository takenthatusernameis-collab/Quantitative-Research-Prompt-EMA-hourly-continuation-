# EMA Hourly Continuation — CVX/USDT P26_34

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.2534 |
| net_win_rate | 0.3830 |
| gross_profit_factor | 0.6537 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -11.8894 |
| sortino_ratio | -5.5890 |
| max_drawdown | 0.9993 |
| cagr | -0.9427 |
| net_avg_win | 8.2529 |
| net_avg_loss | -20.2180 |
| avg_hold_time_bars | 2.2321 |
| exposure | 0.1089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
