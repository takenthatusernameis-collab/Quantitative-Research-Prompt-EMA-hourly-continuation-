# EMA Hourly Continuation — OP/USDT P55_144

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.5949 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -3.6419 |
| sortino_ratio | -1.1404 |
| max_drawdown | 0.7471 |
| cagr | -0.4174 |
| net_avg_win | 47.4051 |
| net_avg_loss | -69.4250 |
| avg_hold_time_bars | 11.2935 |
| exposure | 0.2536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
