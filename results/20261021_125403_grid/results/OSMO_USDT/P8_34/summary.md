# EMA Hourly Continuation — OSMO/USDT P8_34

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 812 |
| net_profit_factor | 0.7358 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -4.1520 |
| sortino_ratio | -1.6884 |
| max_drawdown | 0.8852 |
| cagr | -0.5391 |
| net_avg_win | 63.3137 |
| net_avg_loss | -74.5746 |
| avg_hold_time_bars | 8.3239 |
| exposure | 0.3072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
