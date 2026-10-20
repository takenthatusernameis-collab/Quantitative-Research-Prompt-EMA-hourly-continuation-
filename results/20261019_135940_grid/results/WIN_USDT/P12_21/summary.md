# EMA Hourly Continuation — WIN/USDT P12_21

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.1864 |
| net_win_rate | 0.3426 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.3959 |
| sharpe_ratio | -17.6598 |
| sortino_ratio | -10.0841 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 4.5202 |
| net_avg_loss | -12.6328 |
| avg_hold_time_bars | 2.3851 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
