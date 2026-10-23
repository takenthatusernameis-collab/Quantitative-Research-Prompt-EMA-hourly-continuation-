# EMA Hourly Continuation — ZRX/USDT P55_89

**Symbol:** ZRX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.4671 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -6.3809 |
| sortino_ratio | -2.3221 |
| max_drawdown | 0.9448 |
| cagr | -0.6819 |
| net_avg_win | 27.5669 |
| net_avg_loss | -48.3791 |
| avg_hold_time_bars | 4.3979 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
