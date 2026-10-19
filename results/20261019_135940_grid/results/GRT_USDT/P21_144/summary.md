# EMA Hourly Continuation — GRT/USDT P21_144

**Symbol:** GRT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6870 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.7782 |
| sortino_ratio | -0.8784 |
| max_drawdown | 0.6598 |
| cagr | -0.3386 |
| net_avg_win | 58.0069 |
| net_avg_loss | -80.8103 |
| avg_hold_time_bars | 22.2036 |
| exposure | 0.5034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
