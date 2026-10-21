# EMA Hourly Continuation — ONDO/USDT P20_55

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8093 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.5559 |
| sortino_ratio | -0.4786 |
| max_drawdown | 0.5096 |
| cagr | -0.1981 |
| net_avg_win | 78.2026 |
| net_avg_loss | -97.4734 |
| avg_hold_time_bars | 8.6000 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
