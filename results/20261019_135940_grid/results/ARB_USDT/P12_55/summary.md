# EMA Hourly Continuation — ARB/USDT P12_55

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 957 |
| net_profit_factor | 0.5319 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -5.5001 |
| sortino_ratio | -2.3912 |
| max_drawdown | 0.9477 |
| cagr | -0.6866 |
| net_avg_win | 23.5661 |
| net_avg_loss | -40.3262 |
| avg_hold_time_bars | 8.7273 |
| exposure | 0.3796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
