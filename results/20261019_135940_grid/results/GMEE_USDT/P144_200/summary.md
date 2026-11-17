# EMA Hourly Continuation — GMEE/USDT P144_200

**Symbol:** GMEE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.4463 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.7213 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -4.5723 |
| sortino_ratio | -1.2291 |
| max_drawdown | 0.7988 |
| cagr | -0.4524 |
| net_avg_win | 41.0674 |
| net_avg_loss | -67.3654 |
| avg_hold_time_bars | 5.2238 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
