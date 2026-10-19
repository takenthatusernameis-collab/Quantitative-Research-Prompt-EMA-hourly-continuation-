# EMA Hourly Continuation — CRV/USDT P55_144

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -4.0420 |
| sortino_ratio | -1.3328 |
| max_drawdown | 0.8023 |
| cagr | -0.4722 |
| net_avg_win | 47.0463 |
| net_avg_loss | -68.2181 |
| avg_hold_time_bars | 9.0766 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
