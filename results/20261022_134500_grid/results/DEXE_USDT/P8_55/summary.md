# EMA Hourly Continuation — DEXE/USDT P8_55

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.4474 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.7660 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -6.5456 |
| sortino_ratio | -2.7887 |
| max_drawdown | 0.9675 |
| cagr | -0.7443 |
| net_avg_win | 19.2480 |
| net_avg_loss | -33.9971 |
| avg_hold_time_bars | 14.1128 |
| exposure | 0.5915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
