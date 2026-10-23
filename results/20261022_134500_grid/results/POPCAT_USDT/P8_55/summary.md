# EMA Hourly Continuation — POPCAT/USDT P8_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8135 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -5.3760 |
| sortino_ratio | -2.3866 |
| max_drawdown | 0.9152 |
| cagr | -0.6808 |
| net_avg_win | 34.8984 |
| net_avg_loss | -48.1511 |
| avg_hold_time_bars | 11.3693 |
| exposure | 0.5171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
