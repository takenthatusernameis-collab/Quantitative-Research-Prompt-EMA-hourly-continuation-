# EMA Hourly Continuation — ONE/USDT P26_144

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6692 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -3.0014 |
| sortino_ratio | -0.8942 |
| max_drawdown | 0.6660 |
| cagr | -0.3490 |
| net_avg_win | 62.9517 |
| net_avg_loss | -82.4086 |
| avg_hold_time_bars | 25.6916 |
| exposure | 0.5302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
