# EMA Hourly Continuation — TRB/USDT P50_144

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.5245 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8158 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -4.7257 |
| sortino_ratio | -1.5097 |
| max_drawdown | 0.8431 |
| cagr | -0.5139 |
| net_avg_win | 40.7112 |
| net_avg_loss | -60.7612 |
| avg_hold_time_bars | 12.3965 |
| exposure | 0.2900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
