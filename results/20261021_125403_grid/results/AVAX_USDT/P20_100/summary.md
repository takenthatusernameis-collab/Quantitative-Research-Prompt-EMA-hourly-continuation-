# EMA Hourly Continuation — AVAX/USDT P20_100

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.8547 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0795 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.2127 |
| sortino_ratio | -0.3710 |
| max_drawdown | 0.4487 |
| cagr | -0.1588 |
| net_avg_win | 88.5388 |
| net_avg_loss | -110.1838 |
| avg_hold_time_bars | 18.0264 |
| exposure | 0.3720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
