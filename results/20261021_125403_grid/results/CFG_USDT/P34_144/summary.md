# EMA Hourly Continuation — CFG/USDT P34_144

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8787 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.8058 |
| sortino_ratio | -0.5045 |
| max_drawdown | 0.4859 |
| cagr | -0.2076 |
| net_avg_win | 70.4251 |
| net_avg_loss | -83.3584 |
| avg_hold_time_bars | 21.1886 |
| exposure | 0.3727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
