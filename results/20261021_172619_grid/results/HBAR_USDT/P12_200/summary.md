# EMA Hourly Continuation — HBAR/USDT P12_200

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.8816 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0609 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -0.6396 |
| sortino_ratio | -0.1577 |
| max_drawdown | 0.3262 |
| cagr | -0.0728 |
| net_avg_win | 84.1492 |
| net_avg_loss | -102.8413 |
| avg_hold_time_bars | 54.7763 |
| exposure | 0.7345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
