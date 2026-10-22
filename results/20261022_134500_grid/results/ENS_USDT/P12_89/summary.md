# EMA Hourly Continuation — ENS/USDT P12_89

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6357 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -4.0224 |
| sortino_ratio | -1.4847 |
| max_drawdown | 0.8507 |
| cagr | -0.5106 |
| net_avg_win | 44.2202 |
| net_avg_loss | -63.3968 |
| avg_hold_time_bars | 18.6130 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
