# EMA Hourly Continuation — CTC/USDT P12_144

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.8936 |
| net_win_rate | 0.5301 |
| gross_profit_factor | 1.1125 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -0.6542 |
| sortino_ratio | -0.1918 |
| max_drawdown | 0.4038 |
| cagr | -0.0888 |
| net_avg_win | 79.5457 |
| net_avg_loss | -100.4273 |
| avg_hold_time_bars | 34.9036 |
| exposure | 0.6584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
