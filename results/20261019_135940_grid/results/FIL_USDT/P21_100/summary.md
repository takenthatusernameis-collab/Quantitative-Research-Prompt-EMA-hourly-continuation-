# EMA Hourly Continuation — FIL/USDT P21_100

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5326 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -5.4258 |
| sortino_ratio | -1.9670 |
| max_drawdown | 0.9141 |
| cagr | -0.6118 |
| net_avg_win | 35.5182 |
| net_avg_loss | -51.8907 |
| avg_hold_time_bars | 12.8977 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
