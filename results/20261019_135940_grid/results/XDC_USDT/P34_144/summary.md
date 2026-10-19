# EMA Hourly Continuation — XDC/USDT P34_144

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.3195 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.6951 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -7.0625 |
| sortino_ratio | -2.5163 |
| max_drawdown | 0.9627 |
| cagr | -0.7279 |
| net_avg_win | 16.3601 |
| net_avg_loss | -37.9968 |
| avg_hold_time_bars | 11.5787 |
| exposure | 0.3410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
