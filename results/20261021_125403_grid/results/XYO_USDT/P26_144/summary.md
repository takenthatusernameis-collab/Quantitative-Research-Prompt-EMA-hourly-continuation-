# EMA Hourly Continuation — XYO/USDT P26_144

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6606 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -2.9129 |
| sortino_ratio | -0.8388 |
| max_drawdown | 0.6361 |
| cagr | -0.3211 |
| net_avg_win | 64.9104 |
| net_avg_loss | -80.9414 |
| avg_hold_time_bars | 22.1425 |
| exposure | 0.4148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
