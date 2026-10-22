# EMA Hourly Continuation — FIDA/USDT P50_144

**Symbol:** FIDA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6577 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.5615 |
| sortino_ratio | -0.7297 |
| max_drawdown | 0.5825 |
| cagr | -0.2853 |
| net_avg_win | 58.7155 |
| net_avg_loss | -77.2873 |
| avg_hold_time_bars | 15.1241 |
| exposure | 0.2758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
