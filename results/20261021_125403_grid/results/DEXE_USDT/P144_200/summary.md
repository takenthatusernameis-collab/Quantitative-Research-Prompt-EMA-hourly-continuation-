# EMA Hourly Continuation — DEXE/USDT P144_200

**Symbol:** DEXE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7615 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -2.0858 |
| sortino_ratio | -0.3763 |
| max_drawdown | 0.3726 |
| cagr | -0.1602 |
| net_avg_win | 65.6186 |
| net_avg_loss | -91.2101 |
| avg_hold_time_bars | 18.3354 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
