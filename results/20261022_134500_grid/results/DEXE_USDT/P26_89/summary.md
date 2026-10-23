# EMA Hourly Continuation — DEXE/USDT P26_89

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.5820 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -4.0376 |
| sortino_ratio | -1.3936 |
| max_drawdown | 0.8183 |
| cagr | -0.4853 |
| net_avg_win | 40.4889 |
| net_avg_loss | -60.6567 |
| avg_hold_time_bars | 17.4240 |
| exposure | 0.4744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
