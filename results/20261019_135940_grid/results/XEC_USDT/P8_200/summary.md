# EMA Hourly Continuation — XEC/USDT P8_200

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.9525 |
| sortino_ratio | -0.9176 |
| max_drawdown | 0.6843 |
| cagr | -0.3570 |
| net_avg_win | 52.3675 |
| net_avg_loss | -77.7733 |
| avg_hold_time_bars | 34.0264 |
| exposure | 0.7591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
