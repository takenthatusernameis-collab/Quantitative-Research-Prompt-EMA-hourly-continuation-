# EMA Hourly Continuation — CFX/USDT P12_20

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8584 |
| net_win_rate | 0.5524 |
| gross_profit_factor | 1.2227 |
| gross_win_rate | 0.5524 |
| sharpe_ratio | -0.7189 |
| sortino_ratio | -0.1646 |
| max_drawdown | 0.2581 |
| cagr | -0.0733 |
| net_avg_win | 77.0544 |
| net_avg_loss | -110.7872 |
| avg_hold_time_bars | 5.5685 |
| exposure | 0.0628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
