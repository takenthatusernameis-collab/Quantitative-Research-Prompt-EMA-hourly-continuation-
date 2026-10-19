# EMA Hourly Continuation — XDC/USDT P21_50

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.1964 |
| net_win_rate | 0.3872 |
| gross_profit_factor | 0.5903 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -12.0064 |
| sortino_ratio | -5.5445 |
| max_drawdown | 0.9994 |
| cagr | -0.9476 |
| net_avg_win | 6.0315 |
| net_avg_loss | -19.4020 |
| avg_hold_time_bars | 4.4675 |
| exposure | 0.2124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
