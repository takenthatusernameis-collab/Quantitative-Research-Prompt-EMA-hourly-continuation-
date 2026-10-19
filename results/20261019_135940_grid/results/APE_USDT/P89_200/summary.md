# EMA Hourly Continuation — APE/USDT P89_200

**Symbol:** APE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9287 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -2.8680 |
| sortino_ratio | -0.8317 |
| max_drawdown | 0.6336 |
| cagr | -0.3288 |
| net_avg_win | 46.8544 |
| net_avg_loss | -73.8428 |
| avg_hold_time_bars | 9.9340 |
| exposure | 0.1915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
