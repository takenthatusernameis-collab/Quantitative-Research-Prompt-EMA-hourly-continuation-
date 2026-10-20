# EMA Hourly Continuation — MOVR/USDT P34_144

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.5682 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -3.8035 |
| sortino_ratio | -1.2469 |
| max_drawdown | 0.7836 |
| cagr | -0.4454 |
| net_avg_win | 41.4881 |
| net_avg_loss | -60.0324 |
| avg_hold_time_bars | 15.2928 |
| exposure | 0.3775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
