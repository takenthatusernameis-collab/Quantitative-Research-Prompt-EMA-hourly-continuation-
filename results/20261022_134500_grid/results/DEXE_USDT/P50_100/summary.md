# EMA Hourly Continuation — DEXE/USDT P50_100

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.8936 |
| sortino_ratio | -1.2475 |
| max_drawdown | 0.7887 |
| cagr | -0.4492 |
| net_avg_win | 35.1622 |
| net_avg_loss | -60.8872 |
| avg_hold_time_bars | 14.3638 |
| exposure | 0.3356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
