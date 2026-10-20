# EMA Hourly Continuation — AMP/USDT P89_144

**Symbol:** AMP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.2529 |
| net_win_rate | 0.3631 |
| gross_profit_factor | 0.5678 |
| gross_win_rate | 0.3934 |
| sharpe_ratio | -9.1360 |
| sortino_ratio | -3.4038 |
| max_drawdown | 0.9880 |
| cagr | -0.8270 |
| net_avg_win | 13.2677 |
| net_avg_loss | -29.9126 |
| avg_hold_time_bars | 4.8026 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
