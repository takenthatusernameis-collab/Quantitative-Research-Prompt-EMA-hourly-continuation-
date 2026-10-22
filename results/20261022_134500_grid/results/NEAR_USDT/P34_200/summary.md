# EMA Hourly Continuation — NEAR/USDT P34_200

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8008 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0343 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.2469 |
| sortino_ratio | -0.3293 |
| max_drawdown | 0.3708 |
| cagr | -0.1445 |
| net_avg_win | 74.4680 |
| net_avg_loss | -95.7300 |
| avg_hold_time_bars | 32.5710 |
| exposure | 0.5108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
