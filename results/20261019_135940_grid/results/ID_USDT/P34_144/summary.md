# EMA Hourly Continuation — ID/USDT P34_144

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6244 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.9228 |
| sortino_ratio | -0.9054 |
| max_drawdown | 0.6673 |
| cagr | -0.3493 |
| net_avg_win | 46.6127 |
| net_avg_loss | -70.4709 |
| avg_hold_time_bars | 17.6008 |
| exposure | 0.3871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
