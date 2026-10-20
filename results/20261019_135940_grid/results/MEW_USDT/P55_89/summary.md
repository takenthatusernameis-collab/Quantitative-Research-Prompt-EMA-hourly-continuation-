# EMA Hourly Continuation — MEW/USDT P55_89

**Symbol:** MEW/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5202 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8422 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -5.9261 |
| sortino_ratio | -2.1754 |
| max_drawdown | 0.9313 |
| cagr | -0.6514 |
| net_avg_win | 33.5785 |
| net_avg_loss | -51.2292 |
| avg_hold_time_bars | 4.3791 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
