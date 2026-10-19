# EMA Hourly Continuation — BSV/USDT P55_89

**Symbol:** BSV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4095 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.8409 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -7.8816 |
| sortino_ratio | -3.0444 |
| max_drawdown | 0.9777 |
| cagr | -0.7802 |
| net_avg_win | 21.5913 |
| net_avg_loss | -38.5946 |
| avg_hold_time_bars | 4.3096 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
