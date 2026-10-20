# EMA Hourly Continuation — CFG/USDT P12_20

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1556 |
| net_profit_factor | 0.2454 |
| net_win_rate | 0.3811 |
| gross_profit_factor | 0.5974 |
| gross_win_rate | 0.4036 |
| sharpe_ratio | -13.4590 |
| sortino_ratio | -7.5236 |
| max_drawdown | 0.9999 |
| cagr | -0.9782 |
| net_avg_win | 5.4846 |
| net_avg_loss | -13.7608 |
| avg_hold_time_bars | 2.2641 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
