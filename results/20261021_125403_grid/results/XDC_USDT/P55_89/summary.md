# EMA Hourly Continuation — XDC/USDT P55_89

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6912 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1261 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -1.8728 |
| sortino_ratio | -0.4542 |
| max_drawdown | 0.4228 |
| cagr | -0.1862 |
| net_avg_win | 60.6627 |
| net_avg_loss | -99.0742 |
| avg_hold_time_bars | 6.8256 |
| exposure | 0.0872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
