# EMA Hourly Continuation — FET/USDT P20_200

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.8530 |
| net_win_rate | 0.5210 |
| gross_profit_factor | 1.0863 |
| gross_win_rate | 0.5245 |
| sharpe_ratio | -0.7740 |
| sortino_ratio | -0.1867 |
| max_drawdown | 0.2997 |
| cagr | -0.0861 |
| net_avg_win | 78.7612 |
| net_avg_loss | -100.4250 |
| avg_hold_time_bars | 54.8531 |
| exposure | 0.7131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
