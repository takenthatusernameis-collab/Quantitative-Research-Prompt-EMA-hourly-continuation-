# EMA Hourly Continuation — DEXE/USDT P8_100

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9076 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.0957 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.5221 |
| sortino_ratio | -0.1601 |
| max_drawdown | 0.3221 |
| cagr | -0.0763 |
| net_avg_win | 73.9651 |
| net_avg_loss | -91.3970 |
| avg_hold_time_bars | 34.1035 |
| exposure | 0.7038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
