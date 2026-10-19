# EMA Hourly Continuation — XDC/USDT P26_144

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.3324 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.6866 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -6.6775 |
| sortino_ratio | -2.4160 |
| max_drawdown | 0.9575 |
| cagr | -0.7133 |
| net_avg_win | 16.0925 |
| net_avg_loss | -37.6103 |
| avg_hold_time_bars | 13.0517 |
| exposure | 0.4016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
