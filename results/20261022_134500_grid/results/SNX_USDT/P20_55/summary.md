# EMA Hourly Continuation — SNX/USDT P20_55

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -5.6171 |
| sortino_ratio | -2.4562 |
| max_drawdown | 0.9535 |
| cagr | -0.6924 |
| net_avg_win | 30.6020 |
| net_avg_loss | -46.8509 |
| avg_hold_time_bars | 5.3749 |
| exposure | 0.2342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
