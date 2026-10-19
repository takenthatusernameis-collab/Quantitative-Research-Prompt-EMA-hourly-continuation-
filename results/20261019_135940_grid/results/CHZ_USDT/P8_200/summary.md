# EMA Hourly Continuation — CHZ/USDT P8_200

**Symbol:** CHZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0709 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.8374 |
| sortino_ratio | -0.4811 |
| max_drawdown | 0.5181 |
| cagr | -0.2078 |
| net_avg_win | 65.9345 |
| net_avg_loss | -94.9237 |
| avg_hold_time_bars | 50.9143 |
| exposure | 0.8100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
