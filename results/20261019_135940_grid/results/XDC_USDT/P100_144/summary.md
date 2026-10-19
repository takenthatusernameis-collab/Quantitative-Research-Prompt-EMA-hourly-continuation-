# EMA Hourly Continuation — XDC/USDT P100_144

**Symbol:** XDC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.1505 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.5180 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -9.6514 |
| sortino_ratio | -3.3791 |
| max_drawdown | 0.9902 |
| cagr | -0.8413 |
| net_avg_win | 8.0091 |
| net_avg_loss | -31.8462 |
| avg_hold_time_bars | 3.4085 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
