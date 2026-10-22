# EMA Hourly Continuation — APE/USDT P8_34

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1414 |
| net_profit_factor | 0.4534 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -9.0453 |
| sortino_ratio | -4.7873 |
| max_drawdown | 0.9971 |
| cagr | -0.9021 |
| net_avg_win | 13.4680 |
| net_avg_loss | -22.8002 |
| avg_hold_time_bars | 4.9590 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
