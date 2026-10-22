# EMA Hourly Continuation — MNT/USDT P26_89

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.4273 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.7967 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -6.2506 |
| sortino_ratio | -2.2397 |
| max_drawdown | 0.9422 |
| cagr | -0.6760 |
| net_avg_win | 24.6326 |
| net_avg_loss | -44.5262 |
| avg_hold_time_bars | 10.9740 |
| exposure | 0.3262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
