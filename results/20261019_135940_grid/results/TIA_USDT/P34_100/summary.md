# EMA Hourly Continuation — TIA/USDT P34_100

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.7424 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 1.0402 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.5597 |
| sortino_ratio | -0.8703 |
| max_drawdown | 0.6734 |
| cagr | -0.3372 |
| net_avg_win | 64.6605 |
| net_avg_loss | -86.4963 |
| avg_hold_time_bars | 11.6059 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
