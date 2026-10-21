# EMA Hourly Continuation — ZEN/USDT P26_200

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.8103 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.1372 |
| sortino_ratio | -0.2728 |
| max_drawdown | 0.3682 |
| cagr | -0.1201 |
| net_avg_win | 84.4178 |
| net_avg_loss | -100.5639 |
| avg_hold_time_bars | 47.9258 |
| exposure | 0.6165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
