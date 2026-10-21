# EMA Hourly Continuation — ALGO/USDT P55_144

**Symbol:** ALGO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.5466 |
| sortino_ratio | -0.4106 |
| max_drawdown | 0.3981 |
| cagr | -0.1720 |
| net_avg_win | 72.9893 |
| net_avg_loss | -93.9652 |
| avg_hold_time_bars | 15.4448 |
| exposure | 0.2415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
