# EMA Hourly Continuation — ZRO/USDT P20_144

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8323 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9604 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.0620 |
| sortino_ratio | -0.2953 |
| max_drawdown | 0.3020 |
| cagr | -0.1291 |
| net_avg_win | 79.0763 |
| net_avg_loss | -91.8260 |
| avg_hold_time_bars | 31.2244 |
| exposure | 0.5380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
