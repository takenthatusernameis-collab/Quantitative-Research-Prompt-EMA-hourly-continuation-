# EMA Hourly Continuation — FLOKI/USDT P55_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6860 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.5062 |
| sortino_ratio | -0.6794 |
| max_drawdown | 0.5855 |
| cagr | -0.2788 |
| net_avg_win | 67.9560 |
| net_avg_loss | -91.9165 |
| avg_hold_time_bars | 24.3155 |
| exposure | 0.4134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
