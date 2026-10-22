# EMA Hourly Continuation — ETHFI/USDT P20_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7654 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.1731 |
| sortino_ratio | -0.6889 |
| max_drawdown | 0.5755 |
| cagr | -0.2757 |
| net_avg_win | 73.9122 |
| net_avg_loss | -92.4194 |
| avg_hold_time_bars | 24.8762 |
| exposure | 0.5665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
