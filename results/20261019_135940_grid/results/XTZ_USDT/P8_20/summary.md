# EMA Hourly Continuation — XTZ/USDT P8_20

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1724 |
| net_profit_factor | 0.2862 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -13.4300 |
| sortino_ratio | -7.9152 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 5.5060 |
| net_avg_loss | -14.0642 |
| avg_hold_time_bars | 2.9600 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
