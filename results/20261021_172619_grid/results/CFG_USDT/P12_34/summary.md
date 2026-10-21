# EMA Hourly Continuation — CFG/USDT P12_34

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.7487 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -3.3287 |
| sortino_ratio | -0.9758 |
| max_drawdown | 0.6815 |
| cagr | -0.3623 |
| net_avg_win | 49.0395 |
| net_avg_loss | -65.6633 |
| avg_hold_time_bars | 19.7710 |
| exposure | 0.3846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
