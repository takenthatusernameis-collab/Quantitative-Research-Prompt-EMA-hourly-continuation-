# EMA Hourly Continuation — BRETT/USDT P89_144

**Symbol:** BRETT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6342 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9494 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.2405 |
| sortino_ratio | -1.0155 |
| max_drawdown | 0.6944 |
| cagr | -0.3812 |
| net_avg_win | 52.6115 |
| net_avg_loss | -77.4260 |
| avg_hold_time_bars | 5.3836 |
| exposure | 0.1202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
