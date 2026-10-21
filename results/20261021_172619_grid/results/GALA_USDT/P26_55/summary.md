# EMA Hourly Continuation — GALA/USDT P26_55

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.8851 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -2.7228 |
| sortino_ratio | -0.8326 |
| max_drawdown | 0.6460 |
| cagr | -0.3170 |
| net_avg_win | 59.0275 |
| net_avg_loss | -77.2629 |
| avg_hold_time_bars | 6.2505 |
| exposure | 0.1304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
