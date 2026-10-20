# EMA Hourly Continuation — AMP/USDT P12_21

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1879 |
| net_profit_factor | 0.1642 |
| net_win_rate | 0.3151 |
| gross_profit_factor | 0.5016 |
| gross_win_rate | 0.3624 |
| sharpe_ratio | -19.9103 |
| sortino_ratio | -12.4780 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 3.3192 |
| net_avg_loss | -9.2968 |
| avg_hold_time_bars | 2.3236 |
| exposure | 0.1985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
