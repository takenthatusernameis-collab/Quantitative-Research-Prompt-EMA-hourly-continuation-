# EMA Hourly Continuation — ICP/USDT P55_144

**Symbol:** ICP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9545 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -4.0533 |
| sortino_ratio | -1.3008 |
| max_drawdown | 0.8008 |
| cagr | -0.4646 |
| net_avg_win | 46.1139 |
| net_avg_loss | -70.2157 |
| avg_hold_time_bars | 10.5764 |
| exposure | 0.2485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
