# EMA Hourly Continuation — AZERO/USDT P12_144

**Symbol:** AZERO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.7757 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0466 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.5795 |
| sortino_ratio | -0.4492 |
| max_drawdown | 0.4736 |
| cagr | -0.1921 |
| net_avg_win | 70.1888 |
| net_avg_loss | -93.2156 |
| avg_hold_time_bars | 37.1460 |
| exposure | 0.6791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
