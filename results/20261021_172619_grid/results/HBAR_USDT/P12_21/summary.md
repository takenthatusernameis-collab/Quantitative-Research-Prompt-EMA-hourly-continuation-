# EMA Hourly Continuation — HBAR/USDT P12_21

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0247 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.8684 |
| sortino_ratio | -0.4255 |
| max_drawdown | 0.4038 |
| cagr | -0.1774 |
| net_avg_win | 68.6135 |
| net_avg_loss | -101.5343 |
| avg_hold_time_bars | 4.6056 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
