# EMA Hourly Continuation — XDC/USDT P34_55

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.1471 |
| net_win_rate | 0.3559 |
| gross_profit_factor | 0.5320 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -13.0969 |
| sortino_ratio | -5.9113 |
| max_drawdown | 0.9997 |
| cagr | -0.9586 |
| net_avg_win | 5.0544 |
| net_avg_loss | -18.9955 |
| avg_hold_time_bars | 3.2704 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
