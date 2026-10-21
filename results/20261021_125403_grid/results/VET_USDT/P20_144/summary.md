# EMA Hourly Continuation — VET/USDT P20_144

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8514 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -0.9573 |
| sortino_ratio | -0.2734 |
| max_drawdown | 0.3089 |
| cagr | -0.1207 |
| net_avg_win | 77.1722 |
| net_avg_loss | -97.2801 |
| avg_hold_time_bars | 29.0556 |
| exposure | 0.5230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
