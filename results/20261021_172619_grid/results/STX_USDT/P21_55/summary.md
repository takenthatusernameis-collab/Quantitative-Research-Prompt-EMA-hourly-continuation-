# EMA Hourly Continuation — STX/USDT P21_55

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.8257 |
| sortino_ratio | -0.5792 |
| max_drawdown | 0.5184 |
| cagr | -0.2331 |
| net_avg_win | 60.1685 |
| net_avg_loss | -81.4890 |
| avg_hold_time_bars | 8.4338 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
