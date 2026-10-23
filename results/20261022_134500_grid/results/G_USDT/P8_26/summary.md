# EMA Hourly Continuation — G/USDT P8_26

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.4630 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -8.6178 |
| sortino_ratio | -4.4325 |
| max_drawdown | 0.9908 |
| cagr | -0.8841 |
| net_avg_win | 16.6167 |
| net_avg_loss | -29.4226 |
| avg_hold_time_bars | 5.2235 |
| exposure | 0.3134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
